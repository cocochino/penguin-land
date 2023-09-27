'''
Created on Sep 26, 2023

@author: Miho

WebDriver waits for page load but not for CSS animation or JavaScript load.
This test case wait for up to 4 seconds until dynamic text div becomes clickable.
Returns timeout exception.
'''
from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase


class clickDynamicText(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox()
        
    def test_one(self):
        self.driver.get('https://eviltester.github.io/synchole/collapseable.html')
        section = self.driver.find_element_by_css_selector("section.condense") 
        section.click()
        
        '''Below is the original line... harder to read
        element = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#aboutlink")))
        Next line made wait independent and reusable for the next link click step
        '''
        wait = WebDriverWait(self.driver, 4)
        
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#aboutlink")))
        
        element.click()
        
        ''' Two types of testing:
        1. By using TestCase's assertion
        2. By utilizing sync process of wait and timeout exception
        '''
        wait.until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/h1'), 'About The Sync Hole'))
        self.assertTrue(self.driver.current_url.__contains__("about.html"), 'Incorrect URL.')


    def tearDown(self):
        self.driver.close()
