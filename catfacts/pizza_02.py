#!/usr/bin/env python3
"""pizza"""
#from selenium import webdriver

#driver = webdriver.Chrome()

#driver.open("https://dominos.com")


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
browser = webdriver.Firefox(capabilities=cap, executable_path="C:\\path\\to\\geckodriver.exe")
browser.get('http://google.com/')
browser.quit()