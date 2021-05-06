#!/usr/bin/env python
''' Publish data to the channel '''

from paho.mqtt import client as mqtt_client
from random import randint
import time


BROKER = "rabbitmq"
PORT = 1883
TOPIC = "tmp/temp-v2v"
USERNAME = 'test'
PASSWORD = 'test'

def publish(client):
    while True:
        # publish a value each 10 seconds
        time.sleep(10)
        # generate the value temp
        result = client.publish(TOPIC, randint(50, 100))
        status = result[0]

        # validate if it possible to publish the data
        if status == 0:
            print(f"message publish on `{TOPIC}`")
        else:
            print(f"Failed to send message to TOPIC {TOPIC}")

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected to `{TOPIC}`")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(f'python-mqtt-{randint(0, 1000)}')
    client.on_connect = on_connect

    client.username_pw_set(USERNAME, PASSWORD)
    client.connect(BROKER, PORT)

    return client

if __name__ == '__main__':
    client = connect_mqtt()
    client.loop_start()
    publish(client)
