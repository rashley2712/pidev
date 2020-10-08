#!/usr/bin/env python3
# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
# Buzzer on GPIO13
from time import sleep
import subprocess, sys
import datetime

while True:
	readCommand = ["/home/pi/share/pidev/readTsky"]
	result = subprocess.run(readCommand, stdout=subprocess.PIPE)
	Tsky = float(result.stdout.decode('utf-8'))
	readCommand = ["/home/pi/share/pidev/readTamb"]
	#subprocess.call(readCommand)
	
	result = subprocess.run(readCommand, stdout=subprocess.PIPE)
	Tamb = float(result.stdout.decode('utf-8'))
	print(datetime.datetime.now(), "ambient temperature:", Tamb, "sky temperature:", Tsky)
	sys.stdout.flush()
	sleep(60)
