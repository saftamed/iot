# ID de l'organisation
# f95doa
# Type de terminal
# raspberry_pi
# ID de terminal
# raspberry
# Méthode d'authentification
# use-token-auth
# Jeton d'authentification
# 5&cLissGtmId4W9mmp

import RPi.GPIO as GPIO
import Adafruit_DHT
import json
import paho.mqtt.client as mqtt
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

sensor = Adafruit_DHT.DHT11
pin = 17

pubTopic1 = "iot-2/evt/send/fmt/json";

def on_connect(client,userdata,flags,rc):
	print("connected To The Server !!")

def on_message(client,userdata,msg):
	l=json.loads(msg.payload)["led"]
	print(l)
	GPIO.output(11,l)


client = mqtt.Client('d:f95doa:raspberry_pi:raspberry')

client.username_pw_set('use-token-auth', '5&cLissGtmId4W9mmp')
client.connect('f95doa.messaging.internetofthings.ibmcloud.com', 1883, 60)

client.subscribe("iot-2/cmd/led/fmt/json")
client.on_connect = on_connect
client.on_message = on_message

while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	if humidity is not None and temperature is not None:
		client.publish(pubTopic1,json.dumps({"d":{"temperature":temperature,"humidity":humidity}}))
	client.loop()
	time.sleep(1)

client.disconnect()