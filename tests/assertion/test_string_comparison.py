'''
Created on Sep 10, 2023

@author: Miho

Assertion example - Run this as PyUnit
'''
from selenium import webdriver
from unittest import TestCase

class sanityCheck(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox()
        self.driver.get('http://www.google.com')
        
    def test_one(self):
        self.assertEqual("Mooshu", "Mooshu")

    def tearDown(self):
        self.driver.close()
        