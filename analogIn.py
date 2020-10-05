#!/usr/bin/env python3
# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
 
chan = AnalogIn(ads, ADS.P1)
 
while True:
	print(chan.value, chan.voltage)
	sleep(.5)
