import ssl
import sys

import paho.mqtt.client

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='bb', qos=0)

def on_message(client, userdata, message):
	if r1
	print('------------------------------')
	print('topic: %s' % message.topic)
	print('payload: %s' % message.payload)
	print('qos: %d' % message.qos)

def main():
	client = paho.mqtt.client.Client(client_id='safta', clean_session=False)
	#client.username_pw_set('[username]', '[password]')
	client.on_connect = on_connect
	client.on_message = on_message
	#client.tls_set('/etc/ssl/certs/DST_Root_CA_X3.pem', tls_version=ssl.PROTOCOL_TLSv1_2)
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()

if __name__ == '__main__':
	main()
	sys.exit(0)
