import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess

PIN = 5

def button_activated(channel):
	print("signal falling on pin "+ str(channel))
	pin_status(channel)
	subprocess.call(['shutdown', '-h', 'now'], shell=False)

def pin_status(channel):
	if GPIO.input(channel) == GPIO.LOW :
	        print('input low')
	else:
        	print('input high')

GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

pin_status(PIN)

# detect FALLING on PIN deboucing for 200ms
GPIO.add_event_detect(PIN,GPIO.BOTH,callback=button_activated,bouncetime=300)

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
