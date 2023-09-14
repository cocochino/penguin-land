'''
Created on Sep 11, 2023

@author: Miho

add waits to asynchronous pages
When a webpage is loaded asynchronously, some elements take longer than others to load. 
Waits add a time interval between actions performed by the WebDriver.
'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get("http://www.python.org")

myelem = driver.find_element_by_id('start-shell')


driver.close()