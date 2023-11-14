import RPi.GPIO as GPIO
import requests
import time as t

GPIO.setmode(GPIO.BOARD)
led = 21
pino_sensor_som = 12

URL_twitter = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update'

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

GPIO.setup(pino_sensor_som, GPIO.IN)

def enviar_tweet():
    requests.post(URL_twitter, data={"api_key": "7BUK0GHQAAM4VY8X", "status": "Alerta: som detectado!"})

try:
    while True:
        som_detectado = GPIO.input(pino_sensor_som)

        if som_detectado >= 700:
            GPIO.output(led, GPIO.HIGH)
            enviar_tweet()
        else:
            GPIO.output(led, GPIO.LOW)

        t.sleep(5)

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário!")
    GPIO.cleanup()