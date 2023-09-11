'''
Created on Sep 11, 2023

@author: Miho
Thank you, Python page, to let me try this!

'''
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.python.org")

elem_name_q = driver.find_element_by_name('q')
print("My class element is: ", elem_name_q)

elem_id_q = driver.find_element_by_id("id-search-field")
print("My class element is: ", elem_id_q)

#This is raw xpath
#elem_xpath_what = driver.find_element_by_xpath('/html/body/div/div[3]/div/section/div[2]/div[1]/div/h2/span')
#This is xpath modified with class ID
elem_xpath_what = driver.find_element_by_xpath("//*[@class='icon-news']")
print("My class element is: ", elem_xpath_what)

elem_class = driver.find_element_by_class_name('icon-download')
print("My class element is: ", elem_class)

driver.close()
