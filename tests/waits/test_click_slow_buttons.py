'''
Created on Oct 2, 2023

@author: Miho

Use try-except to check condition of the dynamic buttons and timeout.
Rather than timeout exception, this marks test case as fail if the button won't be activated.
'''

from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase


class waitForSlowButtons(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox()
        
    def test_one(self):
        self.driver.get('https://eviltester.github.io/synchole/buttons.html')
        
        buttons = ['button00', 'button01', 'button02', 'button03']
        for button in buttons:
            self.clickOnDynamicButton(button)

        buttonMsg = self.driver.find_element(By.ID, 'buttonmessage')
        
        self.assertEqual(buttonMsg.text, 'All Buttons Clicked', 'Incorrect message found.')
    
    def clickOnDynamicButton(self, name):
        timeout = 10
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.ID, name)))
            element.click()
        except:
            print(f"The button {name} didn't become active within {timeout} seconds.")
            ''' To mark test as pass, use self.skipTest(reason) '''
            self.fail("Aborting the test case.")        

    def tearDown(self):
        self.driver.close()
