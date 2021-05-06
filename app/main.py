from flask import Flask
import paho.mqtt.client as mqtt

app = Flask(__name__)

topic = 'foo'
port = 5001
USERNAME = 'test'
PASSWORD = 'test'

def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)
    # client.publish(topic2, "STARTING SERVER")
    # client.publish(topic2, "CONNECTED")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
# def on_message(client, userdata, msg):
#     client.publish(topic, "MESSAGE")


@app.route('/')
def hello_world():
    return 'Hello World! I am running on port ' + str(port)

if __name__ == '__main__':
    client = mqtt.Client()
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(USERNAME, PASSWORD)
    client.connect('localhost', 1883, 60)
    client.loop_start()

    app.run(host='0.0.0.0', port=port)
