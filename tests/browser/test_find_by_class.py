'''
Created on Sep 11, 2023

@author: Miho

Locating items by HTML class
 - Specifies one or more class name
 - The first element with matching attribute is returned
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('file://C:/WebDriver/test_files/form_sample.html')

elm = driver.find_element_by_class_name('sample_form')
print("Web element is: ", elm)

driver.close()
