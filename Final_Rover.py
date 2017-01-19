import time
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

print("Setting up GPIOs ...")

GPIO.setwarnings(False)

leftPIN = 22
rightPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftPIN, GPIO.OUT)
GPIO.setup(rightPIN, GPIO.OUT)
print("  ...Assigned PINs")

#setting GPIO17 & GPIO27 as PWM with 100Hz
#Initilization (Giving the ESC a signal)
l = GPIO.PWM(leftPIN, 100)
l.start(10)
time.sleep(0.5)

r = GPIO.PWM(rightPIN, 100)
r.start(10)
time.sleep(0.5)

print("  ...Assigned variables")

#setting up speed variables
rs = 5
rs = 5
print("  ...Created position variables")
print("  ...[Done]")

#platform system processes
print("Defining functions ...")
def help():
	print
	print("Commands:")
	print
	print("========================================================")
	print
	print("left or l		Steers to the left.")
	print("right or r		Steers to the right.")
	print
	print("fast or f		Accellerates the Rover")
	print("slow or s		Decellerates the Rover")
	print
	print("brake or b		Pulling the brakes.")
	print
	print("info			Gives out speedinformation.")
	print("help			That's how you got here.")
	print("exit			Stopping all movements s but remaining in position.")
	print
	print("========================================================")
	print
	print("Script created by Piet.")
	print

main_loop = 1

while main_loop=1:
	#Defining steering
	if command == ("left") or ("l"):
		l.ChangeDutyCycle(12.5)
		r.ChangeDutyCycle(7.5)
		speed = 10
		command = raw_input("?")

	elif command == ("right") or ("r"):
		l.ChangeDutyCycle(7.5)
		r.ChangeDutyCycle(12.5)
		speed = 10
		command = raw_input("?")

	elif command == ("fast") or ("f"):
		if speed+2.5 < 22.5:
			speed = speed + 2.5
			l.ChangeDutyCycle(speed)
			r.ChangeDutyCycle(speed)
		else:
			print("You can't go any faster!")
		command = raw_input("?")

	elif command == ("slow") or ("s"):
		if speed-2.5 > 7.5:
			speed = speed - 2.5
			l.ChangeDutyCycle(speed)
			r.ChangeDutyCycle(speed)﻿
		else:
			print("You are already standing still.")
		command = raw_input("?")

	elif command == ("brake") or ("b"):
		l.ChangeDutyCycle(7.5)
		r.ChangeDutyCycle(7.5)
		speed = 7.5
		command = raw_input("?")

	elif command == ("help"):
		help()
		command = raw_input("?")

	elif command == ("info"):
		if speed = 7.5:
			print("Breaks activated.")
		else speed = 10:
			print("Halting.")
		else 10<speed<22.5:
			print("Driving with roughly 0,192km/h")
		command = raw_input("?")
	
	elif command == ("adminaccess") or ("aa"):
		aa = float(raw_input("set speed: "))
			if 4.5 < vt < 9:
	                        v.ChangeDutyCycle(aa)
        	                v.ChangeDutyCycle(0)
			else:
				print("Please select a Number between 5 and 8.5")
		command = raw_input("?")

	elif command == ("exit") or ("quit"):
		l.ChangedutyCycle(10)
		r.ChangeDutyCycle(10)
		main_loop = 2
GPIO.cleanup()
print("[Done]")

