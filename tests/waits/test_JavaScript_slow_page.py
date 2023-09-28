'''
Created on Sep 28, 2023

@author: Miho

Working with slow loading page that uses JS
When the expected message can't be found, it returns timeout exception.
'''
from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

class waitForSlowJSPage(TestCase):
    
    def setUp(self):
        self.driver= webdriver.Firefox()
        
    def test_one(self):
        self.driver.get('https://eviltester.github.io/synchole/messages.html')
        
        ''' Wait for the JavaScript finish loading messages 
        Step 1. Use expected condition to check for the presence of process completion message
        Step 2. Use JS Executor to check that all process is done. '''
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'messagecount'),'Message Count: 0 : 0'
            )
        )
        page_status = self.driver.execute_script("return (window.totalMessagesReceived>0 && window.renderingQueueCount==0)")
        self.assertTrue(page_status,'JavaScript has not been completed.')
        
        '''  Working with dynamic condition of request traffic'''
        total_sent = self.driver.execute_script("return window.totalRequestsMade")
        total_received = self.driver.execute_script("return window.totalMessagesReceived")
        total_display = self.driver.execute_script("return window.allMessages.length")
        #print(total_sent)
        #print(total_received)
        #print(total_display)
        self.assertEquals(total_display, (total_sent*2 + total_received), 'Displayed message count is not matching.')        

    def tearDown(self):
        self.driver.close()
