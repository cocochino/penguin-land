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

driver.get('file:///C:/Users/Miho/eclipse-workspace/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH03/03_02/html_code_03_02.html')

select = Select(driver.find_element_by_name('numReturnSelect'))

select.select_by_index(4)
time.sleep(2)

select.select_by_visible_text('200')
time.sleep(2)

select.select_by_value('250')
time.sleep(2)

options = select.options
print(options)
time.sleep(2)

submit_btn = driver.find_element_by_name('continue')
submit_btn.submit()
time.sleep(2)

driver.close()