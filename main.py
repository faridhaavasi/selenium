from selenium import webdriver
from selenium.webdriver.common.by import By
from pandas import *
import time
se_str = 'Trade'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://newregister.bcci.bg/edipub')
btn = driver.find_element(By.ID, 'bLang')
time.sleep(3)
btn.click()
s = driver.find_element(by='id', value='BusinessActivity')
s.send_keys(f'{se_str}')
btn = driver.find_element(by='id', value='bSearch')
btn.click()
time.sleep(4)
#inputs = driver.find_elements(By.TAG_NAME, "input")
#checkboxes = driver.find_elements(By.CLASS_NAME, "customer")
# for j in checkboxes:
#         j.click()
#         time.sleep(3)
    
# d = driver.find_element(By.CLASS_NAME, 'pagerButtonR')
# d.click()
c = 0
#pagerButtonR
#10986

for i in range(0, 2):
    i +=10
    table = driver.find_element(By.TAG_NAME, 'table')    

    a=driver.find_elements(By.TAG_NAME, 'a')
    for item in a:
        if '@' in item.text and item.text in table.text:

            print('email:',item.text)
            with open('Trade.text', 'a') as f:
                f.write(item.text)
                f.write('\n') 
    

 
       
    
    try:        
        next_key = driver.find_element(By.CLASS_NAME, 'pagerButtonR')
        time.sleep(4)
        next_key.click()
    except:
        continue


time.sleep(7200)


