import urllib.request
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import threading
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

try:
  # Selenium configuration
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument("--disable-gpu")  # Necessary on some systems
  chrome_options.add_argument("--window-size=1920,1080")  # Window size
  driver_path = 'C:/Users/videowall_03/Documents/sgirpcpython/chromedriver-win64/chromedriver-win64/chromedriver.exe'
  service = ChromeService(executable_path=driver_path)

  # URLs and file paths
  url = "http://localhost:8080/estacionesMet/control/cargaSgirpc.php"

  # Create a Selenium WebDriver instance
  driver = webdriver.Chrome(service=service, options=chrome_options)

  # Access the page with Selenium
  driver.get(url)
  print("Acceso a la página...")
  driver.implicitly_wait(50)
  time.sleep(5)
  driver.close()

  # Close the browser
  driver.quit()

  print("Se han abierto la pestaña cargaSgirpc.php en el navegador de Chrome para la carga de datos en la base SQL")
except:
  print("No se logro la carga de datos en la base SQL debido a algún fallo, revise la conexión a internet o el programa cargaSgirpc.php ")
  # Close the browser
  driver.quit()

final=datetime.now()
print(final)
