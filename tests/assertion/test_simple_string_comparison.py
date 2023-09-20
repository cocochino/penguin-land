'''
Created on Sep 20, 2023

@author: Miho

This file uses selenium.webdriver.support.select to work with dropdown.
It will obtain currently selected item from the dropdown and compare it with expected value.
Run this as PyUnit
'''
from selenium import webdriver;
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from unittest import TestCase

class selectAndVerifyDropdown(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox();
        self.driver.get('file://C:/WebDriver/test_files/dropdown.html');
        self.driver.implicitly_wait(5)
        
    def test_one(self):
        selector = Select(self.driver.find_element_by_name('townsSelect'))
        selector.select_by_index(4)
        
        o = selector.first_selected_option
        selectedoption = o.text
        
        print('name is', selectedoption)
        self.assertEqual("Amherst",  selectedoption)
        

    def tearDown(self):
        self.driver.close()
        