'''
Created on Sep 11, 2023

@author: Miho
Demo of various control methods
'''

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Go to https://wiki.python.org/moin/FrontPage
driver = webdriver.Firefox()
driver.get("https://wiki.python.org/moin/FrontPage")

# Perform search for the text "Beginner"
elem = driver.find_element_by_id("searchinput")
elem.clear()
elem.send_keys("Beginner")
time.sleep(4)
elem.send_keys(Keys.RETURN)
time.sleep(5)

# Left side menu bar, change the value of the select from More Options to Raw Text
# This is the complete xpath
#select = Select(driver.find_element_by_xpath("/html/body/div[2]/div[3]/ul/li[5]/form/div/select"))
select = Select(driver.find_element_by_xpath("//*/form/div/select"))

options = select.options
print(options)

select.select_by_visible_text('Raw Text')
time.sleep(4)

driver.close()