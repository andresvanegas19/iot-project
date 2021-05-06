from flask import Flask
import paho.mqtt.client as mqtt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
# from datetime import date
# import datetime
import datetime
import itertools
import time
from flask import Response, redirect,  url_for

datetime.datetime.utcnow()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:pass@localhost:5432/db"
db = SQLAlchemy(app)

migrate = Migrate(app, db)
port = 5001
topic = 'foo'
port = 5001
USERNAME = 'test'
PASSWORD = 'test'


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


@app.route('/')
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for i, c in enumerate(itertools.cycle('\|/-')):
                yield "data: %s %d\n\n" % (c, i)
                time.sleep(.1)  # an artificial delay
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))


@app.route('/reportes', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        Reporte.query.delete()
        db.session.commit()
        return {}


@app.route('/reportes', methods=['GET'])
def get_reports():
    if request.method == 'GET':
        return {"reportes": [{"metrica": reporte.metrica, "date": reporte.date} for reporte in Reporte.query.all()]}


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)


def on_message(client, userdata, msg):
    reporte = Reporte(metrica=int(msg.payload))
    db.session.add(reporte)
    db.session.commit()
    print(type(int(msg.payload)) == type(1))
    # print(msg.topic+" "+str(msg.payload))


# @app.route('/')
# def pin():
#     return 'Hello World! I am running on port ' + str(port)

# Custom Error Helper Functions
def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response


def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(USERNAME, PASSWORD)
    client.connect('localhost', 1883, 60)
    client.loop_start()

    # db.init_app(app)
    # migrate.init_app(app, db)
    app.run(host='0.0.0.0', port=port)
