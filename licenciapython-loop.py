from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import selenium
import pyodbc
import time

server = 'DESKTOP-40TDACU' 
database = 'DBLicencia' 
username = 'juanma' 
password = 'asdasd123' 
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-40TDACU;'
                      'Database=DBLicencia;'
                      'Trusted_Connection=yes;')

def get_chrome_driver():
    path_to_chrome = "C:\scriptlicencias\chromedriver\chromedriver.exe"
    chrome_options = webdriver.ChromeOptions() 
    
    chrome_options.add_experimental_option("detach", True)
    
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    
    return webdriver.Chrome(executable_path = path_to_chrome,
                            options = chrome_options)

cursor = conn.cursor()
cont = 1
while cont != 4:
    query = "SELECT Nombre,Dni,Genero FROM dbo.Tramites WHERE ID = " + str(cont) 
    cursor.execute(query)
    resultado = cursor.fetchall()
    tabla = [list(i) for i in resultado]
    lista = tabla[0]                        

    web = get_chrome_driver()
    web.maximize_window()
    web.get("https://appsb.mardelplata.gob.ar/Consultas/nTurnosWeb/Vistas/FrontEnd/TurnosFiltros.aspx?Cod_Sistema=1&cod_Tramite=44")
    web.find_element(By.NAME, "ctl00$MainContent$txtNroDoc").send_keys(lista[1])
    web.find_element(By.NAME, "ctl00$MainContent$txtNombre").send_keys(lista[0])
    web.find_element(By.NAME, "ctl00$MainContent$txtEMail").send_keys("juanmagwp@gmail.com")
    web.find_element(By.NAME, "ctl00$MainContent$txtTelefono").send_keys("2235635165")
    sel=Select(web.find_element(By.NAME, "ctl00$MainContent$ddlSexo"))
    sel.select_by_visible_text(lista[2])
    captcha = web.find_element(By.NAME, "ctl00$MainContent$txtCaptchaCode")
    if captcha:
        time.sleep(5)
    web.find_element(By.NAME, "ctl00$MainContent$btnConsultaTurno").click()
    time.sleep(5)
    web.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/form/div[3]/div/div[1]/div/table/tbody/tr[3]/td[4]/input").click()
    time.sleep(3)
    web.find_element(By.NAME, "ctl00$MainContent$btnReservarTurno").click()
    time.sleep(5)
    file_name = lista[1] + ".png"
    web.save_screenshot(file_name)
    time.sleep(3)
    web.quit()
    cont = cont + 1