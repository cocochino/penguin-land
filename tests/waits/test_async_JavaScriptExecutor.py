'''
Created on Sep 27, 2023

@author: Miho

Utilize JavaScriptExecutor
'''
from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase


class clickDynamicText(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox()
        
    def test_one(self):
        self.driver.get('https://eviltester.github.io/synchole/collapseable.html')
        
        title = self.driver.find_element_by_css_selector('.synchole > h2:nth-child(1)') 
        
        ''' 
        *** Synchronous script example ***  
        Replace inner text
        ''' 
        new_title = "This is new title!"
        self.driver.execute_script('arguments[0].innerText=arguments[1];', title, new_title)
        print('Text is: ', title.get_attribute('innerText'))
        
        self.assertEquals(title.get_attribute('innerText'), new_title, 'JSExecutor test failed.')

        ''' 
        *** Asynchronous script example ***  
        Replace innerer text after delay of 5 seconds (5000 milliseconds). 
        '''
        another_title = "This is another title!"
        self.driver.execute_async_script('window.setTimeout(function(arguments){'
            'arguments[0].innerText=arguments[1];'
            'arguments[arguments.length-1]();'
            '}, 5000, arguments);', 
            title, another_title)
        print('Text is: ', title.get_attribute('innerText'))
        
        self.assertEquals(title.get_attribute('innerText'), another_title, 'JSExecutor test failed.')


    def tearDown(self):
        self.driver.close()
