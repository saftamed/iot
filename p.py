import json
import paho.mqtt.client as mqtt
import time

pubTopic1 = "saftamed/feeds/tmp";

def on_connect(client,userdata,flags,rc):
	print("connected !!")

def on_message(client,userdata,msg):
	print(json.loads(msg.payload)["led"])


client = mqtt.Client('d:avdzzp:stype:s2')

client.username_pw_set('saftamed', 'aio_ozPw78p0GLNcqWNGFotE2obHLMdg')
client.connect('io.adafruit.com', 1883, 60)

client.on_connect = on_connect
client.on_message = on_message
#client.loop_forever()

payload = {'d':{'temperature':123}}
while True:
       m=  client.publish(pubTopic1,json.dumps({"d":{"temperature":10,"humidity":100,"objectTemp":124,"motor":10}}))
       client.loop()
       print(m)
       time.sleep(1)

client.disconnect()