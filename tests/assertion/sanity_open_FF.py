'''
Created on Sep 10, 2023

@author: Miho

geckodriver path has been added to OS environmental variable
'''
from selenium import webdriver;
#from unittest import TestCase

class sanityCheck():
    
        driver= webdriver.Firefox();
        
        driver.get('http://www.google.com');
        
        #self.assertEqual("Mooshu", "Mooshu")
        driver.close()

