'''
Created on Sep 11, 2023

@author: Miho
Thank you, Python page, to let me try this!

selenium.webdriver.comomn.key will allow
 - send alphanumeric
 - send special characters such as ENTER key 
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("download")
elem.send_keys(Keys.RETURN)
time.sleep(4)

driver.close()