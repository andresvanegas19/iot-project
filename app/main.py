#!/usr/bin/env python3
''' The file that contains all the functions '''


import matplotlib.pyplot as plt
from flask import request, Flask, Response, redirect,  url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import paho.mqtt.client as mqtt

import datetime
import itertools
import time

import csv
import pandas as pd
import numpy as np

import matplotlib
matplotlib.use('Agg')


datetime.datetime.utcnow()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:pass@pubsub:5432/db"
db = SQLAlchemy(app)

migrate = Migrate(app, db)
topic = 'foo'
port = 8000
USERNAME = 'test'
PASSWORD = 'test'
BROKER = 'broker'


class Reporte(db.Model):
    __tablename__ = 'reporte'

    id = db.Column(db.Integer, primary_key=True)
    metrica = db.Column(db.Integer, nullable=False)
    date = db.Column(
        db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, metrica):
        self.metrica = metrica


with app.app_context():
    db.create_all()

def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response


def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response


@app.route('/statistics', methods=['GET'])
def report():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for i, c in enumerate(itertools.cycle('\|/-')):
                reporte = Reporte.query.order_by(Reporte.id.desc()).first()
                db.session.commit()
                yield "data: %s,%s\n\n" % (reporte.metrica, reporte.date)
                time.sleep(3)  # an artificial delay
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))


@app.route('api/analisis', methods=['POST'])
def analisis():
    if request.method == 'POST':
        generate_csv()

        df = pd.read_csv('reporte.csv')

        group_by_temp = df.groupby([df["Reporte"]], as_index=False).count()

        new = group_by_temp.groupby(
            pd.cut(group_by_temp["Reporte"], np.arange(50, 110, 10))).sum()

        name = ["50-60 °C", "60-70 °C", "70-80 °C", "80-90 °C", "90-100 °C"]

        fig, ax = plt.subplots(nrows=1, ncols=1)

        ax.bar(np.arange(len(name)), new["Feacha"], width=0.5, color='blue')
        plt.title("Numero de veces que se reporto el rango de temperatura")
        plt.xticks(np.arange(len(name)), name, size="medium")

        name_file = 'analisis_temp.png'
        fig.savefig(name_file)
        plt.close(fig)

        return {"Exito": f"se guardo el archivo {name_file} con exito"}


@app.route('api/csv', methods=['POST'])
def generate_csv():
    name_file = 'reporte.csv'
    with open(name_file, 'w+') as file_csv:
        filewriter = csv.writer(file_csv, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Feacha', 'Reporte'])

        reportes = Reporte.query.order_by(Reporte.id.desc())
        db.session.commit()

        for reporte in reportes:
            filewriter.writerow(
                [datetime.datetime.timestamp(reporte.date), reporte.metrica])
        file_csv.close()

    return {"Exito": f"se guardo el archivo {name_file} con exito"}


@app.route('api/reportes', methods=['GET'])
def get_reports():
    if request.method == 'GET':
        return {"reportes": [{"metrica": reporte.metrica, "date": reporte.date} for reporte in Reporte.query.all()]}


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)


def on_message(client, userdata, msg):
    reporte = Reporte(metrica=int(msg.payload))
    db.session.add(reporte)
    db.session.commit()
    print(msg.topic+" "+str(msg.payload))


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(USERNAME, PASSWORD)
    client.connect(BROKER, 1883, 60)
    client.loop_start()

    # db.init_app(app)
    # migrate.init_app(app, db)
    app.run(host='0.0.0.0', port=port)
