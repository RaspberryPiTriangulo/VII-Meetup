import time
import RPi.GPIO as GPIO

pin_port = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_port, GPIO.OUT)

while True:

        if User == "ligar" :
                GPIO.output(pin_port, 1)
                time.sleep(1)
        if User == "desligar":
                GPIO.output(pin_port, 0)
                time.sleep(1)
                

GPIO.cleanup()


