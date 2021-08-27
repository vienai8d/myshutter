# myshutter

## Installation

```
sudo pip3 install paho-mqtt
mkdir -p ~/git-clone
cd ~/git-clone
git clone https://github.com/vienai8d/myshutter.git
```

## /etc/rc.local
Add the following to `/etc/rc.local`.
```
MYSHUTTER_DIR=/home/pi/git-clone/myshutter
MYSHUTTER_BEEBOTTE_TOKEN=<MY_IFTTT_TOKEN>
MYSHUTTER_SLACK_WEBHOOK=<MY_WEBHOOK_URL>
sudo /usr/bin/python3 ${MYSHUTTER_DIR}/main.py ${MYSHUTTER_BEEBOTTE_TOKEN} \
  --cacert ${MYSHUTTER_DIR}/mqtt.beebotte.com.pem \
  --slack ${MYSHUTTER_SLACK_WEBHOOK}
```
