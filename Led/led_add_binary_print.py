#!usr/bin/python
#coding:utf-8

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
LED_PIN_SET = [12, 16, 18, 36, 38, 40]

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

setLedpin()

try:
    while True:
        for data in range(64):
            ledDectoBin(data)

except KeyboardInterrupt:
    print("c")

finally:
    GPIO.cleanup()
