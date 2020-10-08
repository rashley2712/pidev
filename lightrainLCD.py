#!/usr/bin/env python3
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from RPLCD import CharLCD
import time
from RPi import GPIO

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
 
lightchan = AnalogIn(ads, ADS.P1)
rainchan = AnalogIn(ads, ADS.P0)
GPIO.cleanup()
#lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=20, rows=4, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=20, rows=4, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])
lcd.clear()
while True:
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
    
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" %time.strftime("%d/%m/%Y"))
    lcd.cursor_pos = (2, 0)
    lightValue = int(lightchan.voltage/3.3 * 100)
    lcd.write_string("Light: %d%%\n" %lightValue)
    rainValue = int(100 - rainchan.voltage/3.3 * 100)
    #print(chan.value, chan.voltage)
    lcd.cursor_pos = (3, 0)
    lcd.write_string("Rain: %d%%\n" %rainValue)
    
    time.sleep(.25)

