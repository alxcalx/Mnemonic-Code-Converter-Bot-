from typing import get_origin
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import csv as csv_




service = Service('/Applications/chromedriver')
#Using Chrome to access web
options = Options()
options.headless = True
driver = webdriver.Chrome(service=service)
# Open the website
driver.get('file:///Users/new/Desktop/thehack/BIP39%20-%20Mnemonic%20Code.html')
strength = Select(driver.find_element_by_id('strength'))
strength.select_by_visible_text('12')
csv = driver.find_element_by_id('csv-tab')
csv.click()
btn = driver.find_element_by_id('btn_generate')
phrase = driver.find_element_by_id('phrase')
data= driver.find_element_by_id('csv_form_control')
prev_seed =''


    
def getnewcode():  
    btn.click()
    phrase.send_keys('')
    time.sleep(.5)
    seed = phrase.get_attribute('value')
    print(seed)
    data.send_keys('')
    values= data.get_attribute('value')
    if values =='':
      getnewcode()
      return
    print(values)
    addresses = list(values.split(","))
    print(addresses)
    address0 =  addresses[4]
    pukey0 = addresses[5]
    prkey0 = addresses[6]
    print(seed)
    print(address0)
    global prev_seed
  #  if prev_seed==seed:
  #    return        
    instance =[address0,seed]
    with open('data.csv','a') as fd:
      fd_writer = csv_.writer(fd)
      fd_writer.writerow(instance) 
   # prev_seed= seed


for x in range(1,1000000):
 driver.delete_all_cookies()
 getnewcode()



 


