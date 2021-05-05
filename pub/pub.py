#!/usr/bin/env python
''' Publish data to the channel '''


# import paho.mqtt.client as mqtt


# client = mqtt.Client()

# client.username_pw_set("test", password="test")

# client.connect("rabbitmq", 1883)


# client.publish("ALSW/temp", "99")

# client.disconnect()



# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


BROKER = "rabbitmq"
PORT = 1883
TOPIC = "python/mqtt"
USERNAME = 'test'
PASSWORD = 'test'

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"number: {msg_count}"
        result = client.publish(TOPIC, msg_count)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Envio de `{msg}` to TOPIC `{TOPIC}`")
        else:
            print(f"Failed to send message to TOPIC {TOPIC}")
        msg_count += 1

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT BROKER!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(f'python-mqtt-{random.randint(0, 1000)}')
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()