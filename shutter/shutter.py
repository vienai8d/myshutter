from argparse import ArgumentParser
import RPi.GPIO as GPIO
import time

PIN_POWER = 4
PIN_UP    = 6
PIN_STOP  = 16
PIN_DOWN  = 26

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_POWER, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_UP   , GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_STOP , GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(PIN_DOWN , GPIO.OUT, initial=GPIO.HIGH)

def flush():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_POWER, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PIN_UP   , GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PIN_STOP , GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(PIN_DOWN , GPIO.OUT, initial=GPIO.LOW)

def cmd(pin_num):
    GPIO.output(pin_num  , GPIO.LOW)
    time.sleep(1)
    GPIO.output(pin_num  , GPIO.HIGH)
    time.sleep(1)

def check():
    print( '=========== STATUS ===========')
    print(f'POWER: {GPIO.input(PIN_POWER)}')
    print(f'UP   : {GPIO.input(PIN_UP)}')
    print(f'STOP : {GPIO.input(PIN_STOP)}')
    print(f'DOWN : {GPIO.input(PIN_DOWN)}')

def cleanup():
    GPIO.cleanup()

def main():
    parser = ArgumentParser()
    parser.add_argument('cmd', choices=['up', 'down', 'stop'])
    args = parser.parse_args()

    setup()

    if args.cmd == 'up':
        cmd(PIN_UP)
    elif args.cmd == 'stop':
        cmd(PIN_STOP)
    elif args.cmd == 'down':
        cmd(PIN_DOWN)

    cleanup()

if __name__ == '__main__':
    main()
