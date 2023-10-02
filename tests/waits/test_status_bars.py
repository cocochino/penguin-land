'''
Created on Oct 2, 2023

@author: Miho

Checks status of multiple progress bars.

'''
from selenium import webdriver;
from selenium.webdriver.common.by import By
from unittest import TestCase
import time


class waitForProgressBar(TestCase):
    
    tasks = ['Task 1', 'Task 2', 'Task 3']
    bars = ['progressbar0', 'progressbar1', 'progressbar2']
    
    def setUp(self):
        self.driver= webdriver.Firefox()
        self.driver.get('https://eviltester.github.io/synchole/shortlived.html')
        
    def test_one(self):   
        self.assertTrue(self.get_bar_status(self.bars[0])>0, f'{self.tasks[0]} should have started')
        self.assertTrue(self.get_bar_status(self.bars[1])>0, f'{self.tasks[1]} should have started')
        self.assertTrue(self.get_bar_status(self.bars[2])<100, f'{self.tasks[2]} should not have completed')
        
        
    def test_two(self):   
        timeout = 20        
        status1 = self.progress_achieved(self.bars[0], 100, timeout)
        status2 = self.progress_achieved(self.bars[1], 100, timeout)
        status3 = self.progress_achieved(self.bars[2], 100, timeout)
        self.assertTrue(status1, f'{self.tasks[0]} did not achieve 100% within 20 sec.')
        self.assertTrue(status2, f'{self.tasks[1]} did not achieve 100% within 20 sec.')
        self.assertTrue(status3, f'{self.tasks[2]} did not achieve 100% within 20 sec.')
                
    def progress_achieved(self, bar, value, timeout):
        t = 0
        progress = 0
        while progress < value and t < timeout:
            time.sleep(1)
            progress = self.get_bar_status(bar)
            t += 1 
            #print(f'Progress = {progress}, t = {t}')
        return progress >= value
                    
    def get_bar_status(self, bar_id):
        current = (self.driver.find_element(By.ID, bar_id)).get_attribute("value")
        return float(current)
      

    def tearDown(self):
        self.driver.close()