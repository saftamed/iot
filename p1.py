import paho.mqtt.client as mqtt
import time
ORG = "avdzzp"
DEVICE_TYPE = "stype"
TOKEN = "?mWNMZVoNXt54sdhC4"
DEVICE_ID = "s2"

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/status1/fmt/json";

authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

while True:
       mqttc.publish(pubTopic1, "{d: {tmp: 82}}")
       print("published")
       time.sleep(5)

