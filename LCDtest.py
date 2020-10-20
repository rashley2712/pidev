#!/usr/bin/env python3
from RPLCD.i2c import CharLCD
from time import sleep
import adafruit_ads1x15.ads1115 as ADS
import busio, board
from adafruit_ads1x15.analog_in import AnalogIn

from RPi import GPIO

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
 
chan = AnalogIn(ads, ADS.P1)


lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)
#CharLCD(numbering_mode=GPIO.BCM, cols=20, rows=4, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])
lcd.clear()

i = 0
currentVoltage = 0
while True:
	voltage = chan.voltage
	sleep(.01)
	if abs(voltage - currentVoltage) < 0.03: continue
	lcd.cursor_pos = (0, 0)
	lcd.write_string("Updates: %d"%i)
	lcd.cursor_pos = (1, 0)
	lcd.write_string("Voltage: %.2f"%voltage)
	i+=1
	currentVoltage = voltage
	
