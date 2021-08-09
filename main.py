from argparse import ArgumentParser
import paho.mqtt.client as mqtt
import json
import requests

from shutter import shutter

def main():
    parser = ArgumentParser()
    parser.add_argument('token')
    parser.add_argument('--topic', default='home/shutter')
    parser.add_argument('--cacert', default='mqtt.beebotte.com.pem')
    parser.add_argument('--slack', help='Slack webhook URL', default=None)

    args = parser.parse_args()

    TOKEN = args.token
    HOSTNAME = "mqtt.beebotte.com"
    PORT = 8883
    TOPIC = args.topic
    CACERT = args.cacert
    SLACK = args.slack

    def post_to_slack(message):
        if SLACK:
            requests.post(SLACK, headers={'content-type': 'application/json'}, data=json.dumps({'text': message}))

    def on_connect(client, userdata, flags, respons_code):
        print(f'status {respons_code}')
        client.subscribe(TOPIC)

    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        data = json.loads(msg.payload.decode("utf-8"))["data"]
        print(data)
        if data == 'open':
            post_to_slack('[INFO] Open myshutter.')
            shutter.setup()
            shutter.cmd(shutter.PIN_UP)
            shutter.cleanup()
        elif data == 'close':
            post_to_slack('[INFO] Close myshutter.')
            shutter.setup()
            shutter.setup()
            shutter.cmd(shutter.PIN_DOWN)
            shutter.cleanup()
        elif data == 'stop':
            post_to_slack('[INFO] Stop myshutter.')
            shutter.setup()
            shutter.cmd(shutter.PIN_STOP)
            shutter.cleanup()

    client = mqtt.Client()
    client.username_pw_set("token:%s"%TOKEN)
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(CACERT)

    try:
        client.connect(HOSTNAME, port=PORT, keepalive=60)
        post_to_slack('[INFO] myshutter is launched.')
        client.loop_forever()
    except Exception as e:
        post_to_slack(f'[ERROR] myshtter is terminated. Error message: {e}.')

if __name__ == '__main__':
    main()
