import RPi.GPIO as GPIO
import time

LED_PIN=0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)

while(True):
    GPIO.output(LED_PIN,GPIO.HIGH)
    print("LED ON")
    time.sleep(1)
    GPIO.output(LED_PIN,GPIO.LOW)
    print("LED OFF")
    time.sleep(1)