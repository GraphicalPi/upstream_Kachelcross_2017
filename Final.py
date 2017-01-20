import time
import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

print("Setting up GPIOs ...")

GPIO.setwarnings(False)

CamPIN = 17
leftPIN = 22
rightPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftPIN, GPIO.OUT)
GPIO.setup(rightPIN, GPIO.OUT)
print("  ...Assigned PINs")

#setting GPIO17 as PWM with 50Hz (Servo)
#setting GPIO22 & GPIO27 as PWM with 100Hz (ESC)
#Initilization
v = GPIO.PWM(CamPIN, 50)
v.start(5)
time.sleep(0.5)
v.ChangeDutyCycle(0)

l = GPIO.PWM(leftPIN, 100)
l.start(10)
time.sleep(0.5)

r = GPIO.PWM(rightPIN, 100)
r.start(10)
time.sleep(0.5)

print("  ...Assigned variables")

#setting up speed variables
speed = 10
vt = 5
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
	print("Cam-Controll")
	print("up or u			Raises 9 up")
	print("down or d		Raises 9 down")
	print("turn or t		Moves to specific position")
	print
	print("ESC-Controll")
	print("left or l		Steers to the left.")
	print("right or r		Steers to the right.")
	print("fast or f		Accellerates the Rover")
	print("slow or s		Decellerates the Rover")
	print("brake or b		Pulling the brakes.")
	print
	print("info			Gives out status of camera position and speed.")
	print("help			That's how you got here.")
	print("exit			Stopping all movements s but remaining in position.")
	print
	print("========================================================")
	print
	print("Script created by Piet.")
	print

main_loop = 1

while main_loop=1:
	#Defining servo-control
	if command == "turn" or "t":
                try:
                        vs = vt
                        vt = float(raw_input("set turn: "))
			if 4.5 < vt < 9:
	                        v.ChangeDutyCycle(vt)
        	                time.sleep(1)
        	                v.ChangeDutyCycle(0)
        	                command = raw_input("?")
			else:
				print("Please select a Number between 5 and 8.5")
				command = raw_input("?")
                except ValueError:  #if input is not a float, programm will not crash
                        print ("You now what numbers are, right?")
                        command = raw_input("?")

	elif command == "up" or "u":
		if vt + 0.5 != 9:
			vt = vt + 0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0.5)
			v.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("There is no space to go up!")
			command = raw_input

	elif command == "down" or "d":
		if vt - 0.5 != 4.5:
			vt = vt - 0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0.5)
			v.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("You can't go down even more!")
			command = raw_input("?")
	
	#Defining steering
	elif command == ("left") or ("l"):
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
		print
		print("Your current position is: "), vt
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
		v.stop()
		main_loop = 2

	elif:
		print("Learn how to write!")
		command = raw_input("?")

GPIO.cleanup()
print("[Done]")

