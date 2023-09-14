'''
Created on Sep 11, 2023

@author: Miho

selenium.webdriver.support.ui.Select class gives option to select items by
 - name (value)
 - order
 - visible text
'''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()

driver.get('file://C:/WebDriver/test_files/dropdown.html')

select = Select(driver.find_element_by_name('townsSelect'))

select.select_by_index(4)#Amherst... index starts from 0

time.sleep(2)

select.select_by_visible_text('Cambridge')
time.sleep(2)

select.select_by_value('5') #Weymouth
time.sleep(2)

options = select.options
print(options)
time.sleep(2)

submit_btn = driver.find_element_by_name('continue')
submit_btn.submit()
time.sleep(2)

driver.close()