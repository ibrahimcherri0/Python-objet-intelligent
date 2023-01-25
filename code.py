import time
import board
import adafruit_dht
import adafruit_veml7700
import psutil
import requests
import RPi.GPIO as GPIO
import time
import busio


GPIO.setmode(GPIO.BCM)
capteur = 23

GPIO.setup(capteur, GPIO.IN)
i2c = busio.I2C(board.SCL, board.SDA)
veml7700 = adafruit_veml7700.VEML7700(i2c)

url = "https://systeme-domotique-default-rtdb.europe-west1.firebasedatabase.app/test.json"
header = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D4)
while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
        payload = '{"Temperature":'+ str(temp) + ',"Humidite":' + str(humidity) +',"Lumiere":'+ str(veml7700.light)
        if GPIO.input(capteur):
          payload = payload + ',"Mouvement":'+ str(time.time()) +'}'
          print ("Mouvement detecte" + time.ctime(time.time()) )
        else:
          payload = payload + '}'
        response = requests.request("PATCH",url, data=payload)
        time.sleep(1)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
   
    time.sleep(0.1)

