#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

servo_pin = 21
duty_cycle = 7.5     # Should be the centre for a SG90

# Configure the Pi to use pin names (i.e. BCM) and allocate I/O
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM channel on the servo pin with a frequency of 50Hz
pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(duty_cycle)

duty_cycle_start = 2.0
duty_cycle_stop =12.0
steps = 25
step_size = (duty_cycle_stop - duty_cycle_start) / steps
#step_size=0.5
duty_cycle = duty_cycle_start 
pwm_servo.ChangeDutyCycle(1)
time.sleep(4)
try:
	for i in range(steps):
		print("duty cycle percentage:", duty_cycle)
		pwm_servo.ChangeDutyCycle(duty_cycle)
		time.sleep(0.5)
		pwm_servo.ChangeDutyCycle(0)
		time.sleep(.5)
		duty_cycle+= step_size
            
except KeyboardInterrupt:
	print("CTRL-C: Terminating program.")
finally:
	print("Cleaning up GPIO...")
	GPIO.cleanup()
