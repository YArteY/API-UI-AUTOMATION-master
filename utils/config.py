import os

#Pruebas de API
BASE_URL = os.getenv("BASE_URL",'https://dummyjson.com') #Variable de entorno que define la URL BASE
DEFAULT_HEADERS = {'Content-Type': 'application/json'} #Headers predeterminados

#Tiempo maximo (en segundos) aceptado por las respuestas
MAX_RESPONSE_TIME_SECONDS = float(os.getenv("MAX_RESPONSE_TIME_SECONDS",3))


# Pruebas de UI
BASE_URL_UI = 'https://www.saucedemo.com/'
Inventory = {"https://www.saucedemo.com/inventory.html"}