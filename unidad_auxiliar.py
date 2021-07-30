#!/usr/bin/python3

import requests
import time
from datetime import datetime
import dht11
import RPi.GPIO

def gardenberry():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN)
    sensor=dht11.DHT11(pin=7)
    REST_API_URL = "https://api.powerbi.com/beta/4de8f685-7e4c-49b3-8012-89fa56ffb564/datasets/3dbaae90-8701-4e8e-b6e8-e09024c7ae17/rows?redirectedFromSignup=1&key=R2kdzAOqVAaFq%2BiJxIrfMwOnxxJW3tZCibQ5scYQX3Mlen6DyCRCNkfBMV4SfqMv%2FAotTqPr%2Bn%2BNZORS4b6FbA%3D%3D"
    requests.post('https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage?chat_id=-1001294855792&text=*** INICIO ***\nEl Programa de monitoreo ha iniciado correctamente.')
    while True:
          time.sleep(3)
          sensor=dht.read()
          temp=sensor.temperature
          hum=sensor.humidity
          now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]
          data = [
          {"temperature" : temp,
           "humidity" : hum,
           "timestamp" : now
          }
          ]
          requests.post(REST_API_URL, json=data)
   
          if temp<21:
             print(data)
             time.sleep(3)
             sensor = dht.read()
             temp = sensor.temperature
             hum = sensor.humidity
             now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]
             data = [
             {"temperature": temp,
              "humidity": hum,
              "timestamp": now
             }
             ]
             requests.post(REST_API_URL, json=data)

             if temp<21:
                print(data)
                requests.post('https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage?chat_id=-1001294855792&text=*** ALERTA ***\nSe ha detectado una condición de baja temperatura.\n Temperatura: {}[°C]'.format(tem))
         
                while temp<21:
                   time.sleep(6)
                   sensor = dht.read()
                   temp = sensor.temperature
                   hum = sensor.humidity
                   now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]
                   data = [
                   {"temperature": temp,
                    "humidity": hum,
                    "timestamp": now
                   }
                   ]
                   requests.post(REST_API_URL, json=data)
             
                   if temp<21:
                      print(data)
                      requests.post('https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage?chat_id=-1001294855792&text=Persiste la condición de baja temperatura.\nTemperatura: {}[°C]'.format(temp))
                
                   else:
                      print(data)
                      requests.post('https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage?chat_id=-1001294855792&text=Se ha restablecido el regimen normal de funcionamiento.\nTemperatura: {}[°C]'.format(temp))
          
             else:
                print(data)
        

          elif temp>25:
             print(data)
             time.sleep(3)
             sensor = dht.read()
             temp = sensor.temperature
             hum = sensor.humidity
             now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]
             data = [
             {"temperature": temp,
              "humidity": hum,
              "timestamp": now
             }
             ]
             requests.post(REST_API_URL, json=data)
           
             if temp>25:
                print(data)
                requests.post('https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage?chat_id=-1001294855792&text=*** ALERTA ***\nSe ha detectado una condición de sobre temperatura.\nTemperatura: {}[°C]'.format(temp))
             
                while temp>25:
                   time.sleep(6)
                   sensor = dht.read()
                   temp = sensor.temperature
                   hum = sensor.humidity
                   now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]
                   data = [
                   {"temperature": temp,
                    "humidity": hum,
                    "timestamp": now
                   }
                   ]
                   requests.post(REST_API_URL, json=data)
          
                   if temp>25:
                      print(data)
                      requests.post('https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage?chat_id=-1001294855792&text=Persiste la condición de sobre temperatura.\nTemperatura: {}[°C]'.format(temp))
                
                   else:
                      print(data)
                      requests.post('https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage?chat_id=-1001294855792&text=Se ha restablecido el regimen normal de funcionamiento.\nTemperatura: {}[°C]'.format(temp))
            
             else:
                print(data)
               

          else:
             print(data)
             continue
             
gardenberry()
