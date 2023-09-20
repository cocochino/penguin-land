'''
Created on Sep 20, 2023

@author: Miho

This file uses selenium.webdriver.support.select to work with dropdown.
Possible options are read through the input file.
It will iterate all the dropdown option list item in the html file.
Run this as PyUnit
'''

from selenium import webdriver;
from selenium.webdriver.support.select import Select
from unittest import TestCase

import csv

class selectAndVerifyDropdownLoop(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox();
        self.driver.get('file://C:/WebDriver/test_files/dropdown.html');
        self.driver.implicitly_wait(5)

        
    def test_one(self):
        selector = Select(self.driver.find_element_by_name('townsSelect'))
        with open('test_townlist.csv', mode='r') as td_file:
            print(f'{"ID":<10}{"Name":<10}')
            for record in td_file:
                id, name = record.split(',')
                selector.select_by_index(int(id)-1)
                o = selector.first_selected_option
                selectedoption = o.text
                print(f'{id:<10}{name:<10}')        
                self.assertEqual(selectedoption, name.strip())       

    def tearDown(self):
        self.driver.close()
        