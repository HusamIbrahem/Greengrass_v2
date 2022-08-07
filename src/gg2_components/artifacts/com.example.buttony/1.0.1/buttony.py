import time
import RPi.GPIO as GPIO
import awsiot.greengrasscoreipc
from awsiot.greengrasscoreipc.model import (
    PublishToTopicRequest,
    PublishMessage,
    BinaryMessage
)

# define hardware
BUTTON_PIN=21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# define ipc
ipc_client = awsiot.greengrasscoreipc.connect()
# send "b4pressed" to "mypi/button"
TOPIC = "mypi/button"
MESSAGE = "b4pressed"
TIMEOUT = 10


def publish(topic, message):
    request = PublishToTopicRequest()
    request.topic = topic
    publish_message = PublishMessage()
    publish_message.binary_message = BinaryMessage()
    publish_message.binary_message.message = bytes(message, "utf-8")
    request.publish_message = publish_message
    operation = ipc_client.new_publish_to_topic()
    operation.activate(request)
    future = operation.get_response()
    future.result(TIMEOUT)


def my_callback(channel):
    print('button pressed')
    publish(TOPIC, MESSAGE)


print("button event detect started")

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=my_callback, bouncetime=200)

# Keep the main thread alive, or the process will exit.
while True:
    pass
