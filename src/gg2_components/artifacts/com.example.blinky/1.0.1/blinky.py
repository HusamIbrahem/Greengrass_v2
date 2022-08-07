import RPi.GPIO as GPIO
import time
import sys

#define hardware
LED_PIN=0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)
SLEEPTIME = float(sys.argv[1])


while(True):
    GPIO.output(LED_PIN,GPIO.HIGH)
    print("LED ON")
    time.sleep(SLEEPTIME)
    GPIO.output(LED_PIN,GPIO.LOW)
    print("LED OFF")
    time.sleep(SLEEPTIME)