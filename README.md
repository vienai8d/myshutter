# myshutter

## Installation

```
cd
git clone https://github.com/vienai8d/myshutter.git
```

## /etc/rc.local
Add the following to `/etc/rc.local`.
```
IFTTT_TOKEN=<MY_IFTTT_TOKEN>
WEBHOOK_URL=<MY_WEBHOOK_URL>
sudo /usr/bin/python3 /home/pi/myshutter/main.py ${IFTTT_TOKEN} \
  --cacert /home/pi/myshutter/mqtt.beebotte.com.pem \
  --slack ${WEBHOOK_URL} &
```
