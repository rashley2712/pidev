#!/usr/bin/env python3
from RPLCD import CharLCD
import time
from RPi import GPIO

 

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=20, rows=4, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.clear()
while True:
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
    
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" %time.strftime("%d/%m/%Y"))
    lcd.cursor_pos = (2, 0)
    lcd.write_string("Light: %d" %100)

    time.sleep(.1)

