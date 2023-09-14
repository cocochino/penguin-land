'''
Created on Sep 11, 2023

@author: Miho

Locating items by name
 - Doesn't have to be unique in an HTML document
 - Mostly used in forms to reference the element
 
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('file://C:/WebDriver/test_files/form_sample.html')

elm = driver.find_element_by_name('username')
print("Web element is: ", elm)

driver.close()

