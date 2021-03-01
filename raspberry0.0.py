import json
import paho.mqtt.client as mqtt
import time
import random

pubTopic1 = "iot-2/evt/send/fmt/json";

def on_connect(client,userdata,flags,rc):
	print("connected !!")

def on_message(client,userdata,msg):
	print(json.loads(msg.payload)["led"])


client = mqtt.Client('d:3mda17:python:raspberry')

client.username_pw_set('use-token-auth', 'sMkpaw1&JsaSf9y0lx')
client.connect('3mda17.messaging.internetofthings.ibmcloud.com', 1883, 60)

client.subscribe("iot-2/cmd/led/fmt/json")
client.on_connect = on_connect
client.on_message = on_message

while True:
	temperature =random.randrange(-40,100)
	tempob =random.randrange(30,100)
	tempmotor =random.randrange(40,100)
	humidity =random.randrange(0,100)
	client.publish(pubTopic1,json.dumps({"d":{"temperature":temperature,"humidity":humidity,"objectTemp":tempob,"motor":tempmotor}}))
	client.loop()
	time.sleep(5)

client.disconnect()