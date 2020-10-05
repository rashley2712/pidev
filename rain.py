#!/usr/bin/env python3
# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import InputDevice
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
 
inputPIN = 20
no_rain = InputDevice(18)
GPIO.setmode(GPIO.BCM)

GPIO.setup(inputPIN, GPIO.IN) 
chan = AnalogIn(ads, ADS.P0)
 
while True:
	print(chan.value, chan.voltage)
	if not no_rain.is_active:
		print("It's raining - get the washing in!")
	else:
		print("It isn't raining.")
	sleep(.5)
