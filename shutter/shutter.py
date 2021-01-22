from argparse import ArgumentParser
import RPi.GPIO as GPIO
import time

PIN_POWER = 4
PIN_UP    = 6
PIN_STOP  = 16
PIN_DOWN  = 26

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_POWER, GPIO.OUT)
    GPIO.setup(PIN_UP   , GPIO.OUT)
    GPIO.setup(PIN_STOP , GPIO.OUT)
    GPIO.setup(PIN_DOWN , GPIO.OUT)

def setup_with_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_POWER, GPIO.OUT, initial=GPIO.LOW)
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
    GPIO.output(PIN_POWER, GPIO.HIGH)
    GPIO.output(pin_num  , GPIO.LOW)
    time.sleep(2)
    print('on')
    check()
    GPIO.output(pin_num  , GPIO.HIGH)
    GPIO.output(PIN_POWER, GPIO.LOW)
    time.sleep(2)
    print('off')
    check()

def check():
    print(f'POWER: {GPIO.input(PIN_POWER)}')
    print(f'UP   : {GPIO.input(PIN_UP)}')
    print(f'STOP : {GPIO.input(PIN_STOP)}')
    print(f'DOWN : {GPIO.input(PIN_DOWN)}')

def cleanup():
    GPIO.cleanup()

def main():
    parser = ArgumentParser()
    parser.add_argument('cmd', choices=['check', 'flush', 'up', 'down', 'stop'])
    args = parser.parse_args()

    if args.cmd == 'check':
        setup()
        check()
        return

    if args.cmd == 'flush':
        setup()
        flush()
        return

    setup_with_init()
    check()

    if args.cmd == 'up':
        print('up')
        cmd(PIN_UP)
    elif args.cmd == 'stop':
        print('stop')
        cmd(PIN_STOP)
    elif args.cmd == 'down':
        print('down')
        cmd(PIN_DOWN)

    check()
    cleanup()

if __name__ == '__main__':
    main()
