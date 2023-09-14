'''
Created on Sep 10, 2023

@author: Miho

geckodriver path has been added to OS environmental variable
'''

from selenium import webdriver;
driver= webdriver.Firefox();

driver.get('http://www.google.com');

driver.close()
