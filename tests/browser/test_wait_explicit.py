'''
Created on Sep 11, 2023

@author: Miho

Comparison of wait methods
Explicit waits are used to pause the script until a certain condition has been satisfied.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("http://www.python.org")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "start-shell"))
        )
finally:
    driver.quit()
    
