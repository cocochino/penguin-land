'''
Created on Sep 26, 2023

@author: Miho
This test case waits up to 10 seconds until the dynamic buttons becomes clickable,
then validate that correct message is displayed to the users.
Returns timeout exception.
'''

from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase


class clickDynamicButtons(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox()
        
    def test_one(self):
        self.driver.get('https://eviltester.github.io/synchole/buttons.html')
        
        buttons = ['easy00', 'easy01', 'easy02', 'easy03']
        for button in buttons:
            self.clickOnDynamicButton(button)

        buttonMsg = self.driver.find_element(By.ID, 'easybuttonmessage')
        
        self.assertEqual(buttonMsg.text, 'All Buttons Clicked', 'Incorrect message found.')
    
    def clickOnDynamicButton(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, name)))
        element.click()        

    def tearDown(self):
        self.driver.close()
