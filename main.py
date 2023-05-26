from selenium import webdriver
from selenium.webdriver.common.by import By

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
list_of_emaile = []
for i in range(1, 2):
    i +=10    
    block = driver.find_elements(By.CLASS_NAME, 'grid-cell')
    emails = driver.find_elements(By.TAG_NAME, 'a')
    for email in emails:
        if '@' in email.text:
    
            list_of_emaile.append(email.text)
    try:        
        next_key = driver.find_element(By.CLASS_NAME, 'pagerButtonR')
        time.sleep(4)
        next_key.click()
    except:
        continue
print('----------------------------------------')    
print('resolt:')    
#print(list_of_emaile)
for j in list_of_emaile:
    print(j)

time.sleep(7200)


