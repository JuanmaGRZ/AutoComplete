from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
import io
import selenium
import time

def get_chrome_driver():
    path_to_chrome = "C:\scriptlicencias\chromedriver\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions() 
    
    chrome_options.add_experimental_option("detach", True)
    
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    
    return webdriver.Chrome(executable_path = path_to_chrome,
                            options = chrome_options)

web = get_chrome_driver()
web.maximize_window()
web.get("https://appsb.mardelplata.gob.ar/Consultas/nTurnosWeb/Vistas/FrontEnd/TurnosFiltros.aspx")
cont = 1
while cont != 51:
    captcha = web.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/form/div[3]/div/div/div[6]/div/div/div[1]/div").screenshot_as_png
    imageStream = io.BytesIO(captcha)
    im = Image.open(imageStream)
    im.save(str(cont) + ".png")
    web.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/form/div[3]/div/div/div[6]/div/div/div[2]/a").click()
    time.sleep(1)
    cont = cont + 1