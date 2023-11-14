import RPi.GPIO as GPIO
import requests
import time as t

# Configuração do Raspberry Pi
GPIO.setmode(GPIO.BOARD)
led = 21
pino_sensor_som = 12  # Pino GPIO para o sensor de som

# Configurações do ThingSpeak
URL_twitter = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update'

# Configuração do LED
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

# Configuração do sensor de som
GPIO.setup(pino_sensor_som, GPIO.IN)

def enviar_tweet():
    # Enviar tweet quando o som for detectado
    requests.post(URL_twitter, data={"api_key": "7BUK0GHQAAM4VY8X", "status": "Alerta: som detectado!"})

try:
    while True:
        som_detectado = GPIO.input(pino_sensor_som)

        if som_detectado:
            GPIO.output(led, GPIO.HIGH)  # Acender o LED
            enviar_tweet()
        else:
            GPIO.output(led, GPIO.LOW)  # Desligar o LED

        t.sleep(5)

except KeyboardInterrupt:
    print("Programa encerrado pelo usuário!")
    GPIO.cleanup()
