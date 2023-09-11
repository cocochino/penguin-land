'''
Created on Sep 11, 2023

@author: Miho

Locating items by HTML class
 - Specifies one or more class name
 - The first element with matching attribute is returned
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('file:///C:/Users/Miho/eclipse-workspace/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html')

login_input = driver.find_element_by_class_name('content')
print("My class element is: ", login_input)

driver.close()
