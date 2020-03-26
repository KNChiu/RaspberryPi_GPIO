#!usr/bin/python
# coding:utf-8

import time
import RPi.GPIO as GPIO

LED_PIN_SET = [12, 16, 18, 22, 36, 38]

PWM_PIN = 40
PWM_FREQ = 300

data = ""

def setLedpin():
    GPIO.setmode(GPIO.BOARD)
    for i in LED_PIN_SET:
        GPIO.setup(i, GPIO.OUT)
    print("Led pin set finish",LED_PIN_SET)

def ledDectoBin(decNum):
    binNum = '{:08b}'.format(decNum)
    for i in LED_PIN_SET:
        GPIO.output(i, decNum & 0x1)
        decNum = decNum >> 1

    print( "Led Binary :", binNum)
    time.sleep(0.1)

def ledBinleft(decNum):
    binNum = 0
    global LED_MOVE_UP
    for i in range(decNum):
        binNum = binNum * 2 + 1
    return binNum

setLedpin()

GPIO.setup(PWM_PIN, GPIO.OUT)
pwm = GPIO.PWM(PWM_PIN, PWM_FREQ)
pwm.start(0)
print("PWM pin set :", PWM_PIN, "frequency :", PWM_FREQ, type(pwm))



try:
    while True:

        for LED_CONT in range(0, 70, 10):
            pwm.ChangeDutyCycle(LED_CONT)
            time.sleep(0.01)
            ledDectoBin(ledBinleft(int(LED_CONT / 10)))

        for LED_CONT in range(60, 0, -10):
            pwm.ChangeDutyCycle(LED_CONT)
            time.sleep(0.01)
            ledDectoBin(ledBinleft(int(LED_CONT / 10)))



except KeyboardInterrupt:
    print("c")

finally:
    pwm.stop()
    GPIO.cleanup()
