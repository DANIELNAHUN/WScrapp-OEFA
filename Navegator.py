import msvcrt
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utils import files_utils as fu

estaciones_list = [
    {"id":10, "nombre":'Ilo Bolognesi'},
    {"id":11, "nombre":'Ilo Pacocha'},
    {"id":12, "nombre":'Ilo Jose Pardo'},
  ]
parametros_list =[
  {"id":1, "nombre":'PM2.5'},
  {"id":3, "nombre":'PM10'},
  {"id":4, "nombre":'CO'},
  ]

name_excel=[]

path_download="D:\Descargas"
path_to_move = "D:\Descargas\DataQA"

def open_browser(estaciones, parametros):

  path=os.path.join(path_to_move,"Data")
  fu.delete_directory(path)
  for estacion in estaciones:
    driver = webdriver.Edge("C:\Program Files\Python\msedgedriver.exe")
    url = f"https://desarrollo.oefa.gob.pe/deam/stec/proyecto_ilo/visor_pifa/seriedetiempo/?x={estacion['id']}"
    print(url)
    driver.get(url)
    time.sleep(5)

    #Seleccionar Parametro
    for parametro in parametros:
      search_params = driver.find_element(by = By.XPATH, value='//*[@id="moreControls"]/div[1]/div/div/div[1]')
      search_params.click()
      parametro_string = f'//*[@id="moreControls"]/div[1]/div/div/div[2]/div/div[{parametro["id"]}]'
      param = driver.find_element(by = By.XPATH, value=parametro_string)
      param.click()
      time.sleep(6)

      #Seleccionar fecha
      #Abrir picktimer
      select_fecha = driver.find_element(by = By.XPATH, value='//*[@id="rangofecha"]/div/input[1]')
      select_fecha.click()
      #Seleccionar año
      select_fecha_y = driver.find_element(by = By.XPATH, value='/html/body/div[4]/div[1]/table/thead/tr[2]/th[2]')
      select_fecha_y.click()
      #Desplazar al año 2021
      select_fecha_y_2021 = driver.find_element(by = By.XPATH, value='/html/body/div[4]/div[2]/table/thead/tr[2]/th[1]')
      select_fecha_y_2021.click()
      #seleccionar mes
      select_fecha_m = driver.find_element(by = By.XPATH, value='/html/body/div[4]/div[2]/table/tbody/tr/td/span[1]')
      select_fecha_m.click()
      #Seleccionar dia
      select_fecha_d = driver.find_element(by = By.XPATH, value='/html/body/div[4]/div[1]/table/tbody/tr[1]/td[6]')
      select_fecha_d.click()
      time.sleep(7)

      #Descargamos el excel
      download_excel = driver.find_element(by = By.XPATH, value='//*[@id="downloadData"]')
      download_excel.click()
      time.sleep(7)

      p=fu.eval_directory(path_to_move,"Data")
      file=fu.get_path_file_recient(path_download)
      new_file=fu.move_file(file,p,str(estacion["nombre"])+" - "+parametro["nombre"]+".xlsx")
      name_excel.append(new_file)

      #Descargamos la imagen
      download_img = driver.find_element(by = By.XPATH, value='//*[@id="dygraph-dyDownload"]')
      download_img.click()
      time.sleep(5)

      p=fu.eval_directory(path_to_move,"Data")
      file=fu.get_path_img_recient(path_download)
      new_file=fu.move_file(file,p,str(estacion["nombre"])+" - "+parametro["nombre"]+".png")
      name_excel.append(new_file)

    driver.quit()

open_browser(estaciones_list, parametros_list)
