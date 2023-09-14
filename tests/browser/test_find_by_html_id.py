'''
Created on Sep 11, 2023

@author: Miho

Locating items by HTML ID 
 - At least one character
 - No space character
 - Case sensitive
 - Unique in the document

'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('file://C:/WebDriver/test_files/form_sample.html')

elm = driver.find_element_by_id('submitnForm')
print("Web element is: ", elm)

driver.close()