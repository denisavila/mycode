#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://lms.alta3.com")

time.sleep(4)



# https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip

email_x = driver.find_element_by_xpath('//*[@id="signinEmail"]')
email_x.send_keys("python1@alta3.com")
time.sleep(1)
passw_x = driver.find_element_by_xpath('//*[@id="signinPassword"]')
passw_x.send_keys("python1")
time.sleep(1)
passw_x.send_keys(Keys.RETURN)

