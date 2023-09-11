'''
Created on Sep 11, 2023

@author: Miho

Locating items by name
 - Doesn't have to be unique in an HTML document
 - Mostly used in forms to reference the element
 
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('file:///C:/Users/Miho/eclipse-workspace/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html')

login_input = driver.find_element_by_name('username')
print("My input element is: ", login_input)

driver.close()

