#!/usr/bin/python3

import requests
import time
import datetime
from datetime import datetime
import dht11
import RPi.GPIO as GPIO
import logging
import speedtest
import socket
import platform
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters

inic = datetime.datetime.now()
start_time = time.time()
flag = False
REST_API_URL = "https://api.powerbi.com/beta/4de8f685-7e4c-49b3-8012-89fa56ffb564/datasets/3dbaae90-8701-4e8e-b6e8-e09024c7ae17/rows?redirectedFromSignup=1&key=R2kdzAOqVAaFq%2BiJxIrfMwOnxxJW3tZCibQ5scYQX3Mlen6DyCRCNkfBMV4SfqMv%2FAotTqPr%2Bn%2BNZORS4b6FbA%3D%3D"
url = 'https://api.telegram.org/bot1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w/sendMessage'
dat = {'chat_id': '-1001294855792', 'text': '*** INICIO ***\nEl Programa de monitoreo ha iniciado correctamente. Comandos Disponibles:\n\n/pi - Muestra el status de parametros generales del microcontrolador.\n/red - Muestra el status de parametros de red del microcontrolador.\n/iot - Muestra el status de los dispositivos asociados al microcontrolador.\n/start - Permite iniciar el sistema de monitoreo.\n/stop - Permite detener el sistema de monitoreo.'}
requests.post(url, json=dat)
updater = Updater(token='1730474179:AAGNmv7AWQemlh60HkZdQ4aX_OgDCni0I_w', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def inicio(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="*** INICIO ***\nEl Programa de monitoreo ha iniciado correctamente. Comandos Disponibles:\n\n/pi - Muestra el status de parametros generales del microcontrolador.\n/red - Muestra el status de parametros de red del microcontrolador.\n/iot - Muestra el status de los dispositivos asociados al microcontrolador.\n/start - Permite iniciar el sistema de monitoreo.\n/stop - Permite detener el sistema de monitoreo.")
start_handler = CommandHandler('inicio', inicio, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def pi(update, context):
    second_time=time.time()
    time_elapsed=second_time-start_time
    second=int(time_elapsed)
    mi, se = divmod(second,60)
    ho, mi = divmod(mi,60)
    cpu_temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3
    context.bot.send_message(chat_id=update.effective_chat.id, text="*** PI ***\nPrograma: Gardenberry v1.0\nFecha de Inicio: {}\nHora de Inicio: {}\nTiempo de operacion: {:04d}:{:02d}:{:02d}\nTemperatura CPU: {:.2f} [°C]".format(inic.strftime("%d-%b-%Y"),inic.strftime("%I:%M:%S"),ho,mi,se,cpu_temp))
start_handler = CommandHandler('pi', pi, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def red(update, context):
    test = speedtest.Speedtest()
    down = test.download() / 1e6
    up = test.upload() / 1e6
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ip = s.getsockname()[0]
    gateway = gw[2]
    host = socket.gethostname()
    context.bot.send_message(chat_id=update.effective_chat.id, text="*** RED ***\nHost: {}\nDirección IP: ´{}´\nGateway: ´{}´\nVelocidad bajada: {:.2f} [Mbps]\nVelocidad subida {:.2f} [Mbps]".format(host,ip,gateway,down,up))
start_handler = CommandHandler('red', red, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def iot(update, context):
    Espressif = "/Esp32"
    PyCom = "/WyPi"
    Raspberry = "/PiZero"
    context.bot.send_message(chat_id=update.effective_chat.id, text="*** IoT ***\nEspressif: {}\nPyCom: {}\nRaspberry: {}".format(Espressif,PyCom,Raspberry))
start_handler = CommandHandler('iot', iot, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def Esp32(update, context):
    Sensor1 = '--'
    Sensor2 = '--'
    Sensor3 = '--'
    context.bot.send_message(chat_id=update.effective_chat.id, text="*** Esp32 STATUS ***\nSensor1: {}[A]\nSensor2: {}\nSensor3: {}".format(Sensor1,Sensor2,Sensor3))
start_handler = CommandHandler('Esp32', Esp32, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def WyPi(update, context):
    Sensor1 = '--'
    Sensor2 = '--'
    Sensor3 = '--'
    context.bot.send_message(chat_id=update.effective_chat.id, text="*** Esp32 STATUS ***\nSensor1: {}[A]\nSensor2: {}\nSensor3: {}".format(Sensor1,Sensor2,Sensor3))
start_handler = CommandHandler('WyPi', WyPi, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def PiZero(update, context):
    Sensor1 = '--'
    Sensor2 = '--'
    Sensor3 = '--'
    context.bot.send_message(chat_id=update.effective_chat.id, text="*** Esp32 STATUS ***\nSensor1: {}[A]\nSensor2: {}\nSensor3: {}".format(Sensor1,Sensor2,Sensor3))
start_handler = CommandHandler('PiZero', PiZero, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def start(update, context):
     dat = {'chat_id': '-1001294855792', 'text': '*** START ***\nEl sistema de monitoreo ha sido iniciado.'}
     requests.post(url, json=dat)
     global flag
     flag=True
start_handler = CommandHandler('start', start, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def stop(update, context):
     print("El sistema de monitoreo ha sido detenido")
     dat = {'chat_id': '-1001294855792', 'text': '*** STOP ***\nEl sistema de monitoreo ha sido detenido.'}
     requests.post(url, json=dat)
     global flag
     flag=False
start_handler = CommandHandler('stop', stop, Filters.user(user_id=1669641660))
dispatcher.add_handler(start_handler)
updater.start_polling()

def gardenberry():

    while True:
      time.sleep(1)
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(7, GPIO.IN)

      while flag==True:
          time.sleep(2)
          sensor=dht11.DHT11(pin=7)
          sensor=sensor.read()
          temp=sensor.temperature
          hum=sensor.humidity
          now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")[:-3]
          data = [
          {"temperature": temp,
           "humidity": hum,
           "timestamp": now
          }
          ]
          
          if temp==0:
             time.sleep(1)
             print("false reading")
          
          elif temp in range (1, 18):
             time.sleep(1)
             print(data)
             requests.post(REST_API_URL, json=data)
             dat = {'chat_id': '-1001294855792', 'text': '*** ALERTA ***\nSe ha detectado una condición de baja temperatura.\n Temperatura: {}[°C]'.format(temp)}
             requests.post(url, json=dat)
           
          elif temp in range (25, 60):
             time.sleep(1)
             print(data)
             requests.post(REST_API_URL, json=data)
             dat = {'chat_id': '-1001294855792', 'text': '*** ALERTA ***\nSe ha detectado una condición de sobre temperatura.\nTemperatura: {}[°C]'.format(temp)}
             requests.post(url, json=dat)
          
          else:
             time.sleep(1)
             print(data)
             requests.post(REST_API_URL, json=data)
             
gardenberry()
