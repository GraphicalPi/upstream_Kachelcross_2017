import RPi.GPIO as GPIO
import time

CamPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(CamPIN, GPIO.OUT)

#setting GPIO 17 as PWM with 50Hz
#Initilization (Moving to default positioning)
v = GPIO.PWM(CamPIN, 50)
v.start(5)
time.sleep(0.5)
v.ChangeDutyCycle(0)
vt = 5

print
print("This is the interactive ServoCam-Control-Programm.")
print("If you need help, just ask for it!")
print

#platform system process
def help():
	print
	print("Commands:")
	print
	print("========================================================")
	print
	print
	print("up			Raises 9° up")
	print("down			Raises 9° down")
	print("turn			Moves to specific position")
	print
	print("status			Prints the current positions")
	print("help			That's how you got here")
	print("exit			Stopping all movements s but remaining in position")
	print
	print("========================================================")
	print
	print("Script created by Piet.")
	print
	return 0
	 
command = raw_input("?")

#expecting input
while command != "exit":
	if command == "turn":
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

	elif command == "up":
		if vt + 0.5 != 9:
			vt = vt + 0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0.5)
			v.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("There is no space to go up!")
			command = raw_input

	elif command == "down":
		if vt - 0.5 != 4.5:
			vt = vt - 0.5
			v.ChangeDutyCycle(vt)
			time.sleep(0.5)
			v.ChangeDutyCycle(0)
			command = raw_input("?")
		else:
			print("You can't go down even more!")
			command = raw_input("?")

	elif command == "status":
		print
		print("Your current position is: "), vt
		command = raw_input("?")

	elif command == "stop":
		v.stop(0)
		command = raw_input ("?")

	elif command == "help":
		help()
		command = raw_input ("?")

	else:
		print("Fuck you, learn how to write")
		command = raw_input("?")



v.stop()
h.stop()

GPIO.cleanup()
print("[Done]")
