import paths
import os
import time
from datetime import date, datetime
from bs4 import BeautifulSoup
from selenium import webdriver #version recomendada de selenium==4.9.1 para geckodriver v.0.34.0
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def weatherlinkweb(nombre,url):
    
    # Get date
    now=datetime.now()
    fecha=(now.strftime("%d-%m-%y"))
    print(fecha)
    # Paths
    filetxt = paths.tempo+nombre+".txt"
    print(filetxt)
    filecsv = paths.file+nombre+".csv"
    print(filecsv)
    user=os.getenv('USERWL')
    pwd=os.getenv('PASSWL')

    
    #web_options = Options()
    web_options = FirefoxOptions()
    #binario de firefox
    #web_options.add_argument('--headless')
    web_options.add_argument("--disable-gpu")  # Necessary on some systems
    web_options.add_argument("--window-size=1920,1080")  # Window size
    driver_path_chrome = paths.chromedriver
    #driver_path_firefox = os.getenv('FIREFOXDRIVER')
    #driver_path_firefox = paths.firefoxdriver
    #print(driver_path_firefox)
    service = ChromeService(executable_path=driver_path_chrome)

    # Create a Selenium WebDriver instance 
    driver = webdriver.Chrome(service=service, options=web_options)
    
    # Create a selenium WebDriver instance with firefox
    #Service = FirefoxService(executable_path=driver_path_firefox)
    #driver = webdriver.Firefox(service=Service, options=web_options)

    #time.sleep(5)

    # Access the page with Selenium
    driver.get(url)
    driver.find_element(By.XPATH,'//*[@id="username"]')\
        .send_keys(user)
    driver.find_element(By.XPATH,'//*[@id="password"]')\
        .send_keys(pwd)
    driver.find_element(By.XPATH,'//*[@id="submit"]')\
        .click()
    print("Acceso a la cuenta...")

    # Data query
    time.sleep(2)
    print(url)
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="summary-view"]/i')\
        .click()
    time.sleep(5)



    # Wait for the element with XPATH get all content into the table
    data_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="scroll-container"]'))
    )
    
    #data_container = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/div/div[2]/table[1]/tbody/tr[8]/td[1]'))
    #)
    
    #data_container = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.ID,'summary'))
    #)
    

    # Print the content of the div
    print(data_container.text)

    # Save the data to the text file
    with open(filetxt, 'w', encoding='utf-8') as file:
        file.write(data_container.text)
    

    # Close the browser
    print("Datos de la estacion",nombre,"obtenidos")
    driver.quit()

try:
    test=weatherlinkweb("LALADRILLERA","https://www.weatherlink.com/bulletin/191c4832-5370-43ba-8274-7be9be6517a7")
except Exception as e:
    print('ERROR:',e)

#try:
#    test=weatherlinkweb("LandadeMatamoros","https://www.weatherlink.com/bulletin/45848948-7ad1-4889-9665-35d70f5f60ff")
#except Exception as e:
#    print('ERROR:',e)
