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

driver.get('file:///C:/Users/Miho/eclipse-workspace/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html')

login_form = driver.find_element_by_id('loginForm')
print("My login form element is: ", login_form)

driver.close()