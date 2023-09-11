'''
Created on Sep 11, 2023

@author: Miho
'''
from selenium import webdriver

driver = webdriver.Firefox()


driver.get("http://www.python.org")

myelem = driver.find_element_by_id('start-shell')
driver.implicitly_wait(5)

driver.close()