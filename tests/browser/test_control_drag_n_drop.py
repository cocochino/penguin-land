'''
Created on Sep 11, 2023

@author: Miho

selenium.webdriver.ActionChain class enables working with drag and drop
 - from source to target
 - By offset
 
'''

import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()

driver.get('http://jqueryui.com/droppable')

driver.switch_to.frame(0)

action_chains = ActionChains(driver)

source = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')

action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)
action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()