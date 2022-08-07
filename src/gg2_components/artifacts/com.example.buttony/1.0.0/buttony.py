import time
import RPi.GPIO as GPIO


BUTTON_PIN=21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN,pull_up_down=GPIO.PUD_UP)


def my_callback(channel):
    print('button pressed')


print("button event detect started")

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=my_callback, bouncetime=200)


# Keep the main thread alive, or the process will exit.
while True:
    pass