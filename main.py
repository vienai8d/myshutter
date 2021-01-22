from argparse import ArgumentParser
import paho.mqtt.client as mqtt
import json

from shutter import shutter

def main():
    parser = ArgumentParser()
    parser.add_argument('token')
    parser.add_argument('--topic', default='home/shutter')
    args = parser.parse_args()

    TOKEN = args.token
    HOSTNAME = "mqtt.beebotte.com"
    PORT = 8883
    TOPIC = args.topic
    CACERT = "mqtt.beebotte.com.pem"

    def on_connect(client, userdata, flags, respons_code):
        print('status {0}'.format(respons_code))
        client.subscribe(TOPIC)

    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        data = json.loads(msg.payload.decode("utf-8"))["data"]
        print(data)
        if data == 'open':
            shutter.setup()
            shutter.cmd(shutter.PIN_UP)
            shutter.cleanup()
        elif data == 'close':
            shutter.setup()
            shutter.cmd(shutter.PIN_DOWN)
            shutter.cleanup()
        elif data == 'stop':
            shutter.setup()
            shutter.cmd(shutter.PIN_STOP)
            shutter.cleanup()

    client = mqtt.Client()
    client.username_pw_set("token:%s"%TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(CACERT)
    client.connect(HOSTNAME, port=PORT, keepalive=60)
    client.loop_forever()

if __name__ == '__main__':
    main()
