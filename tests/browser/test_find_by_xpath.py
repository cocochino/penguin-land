'''
Created on Sep 11, 2023

@author: Miho

Locating items by XPATH
 - used path expression and navigate nodes in an XML document
 - Used when ID or name isn't available
 - Either absolute or relative
      - Absolute path is tricky as new elements in the page could change the element order
      - Relative path uses backslash to indicate HTML element level
      - Relative path combined with ID will help aoiding element order problem
'''

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('file:///C:/Users/Miho/eclipse-workspace/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html')

login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
# Belov 2 lines shows two back slash to indicate "skip two levels, then find the first form at the 3rd level"
login_form_relative = driver.find_element_by_xpath("//form[1]")
# Here's example of locating the item with XPATH and ID! More specific
login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']")

print("My input element is: ")
print( login_form_absolute)
print( login_form_relative)
print( login_form_id)
driver.close()