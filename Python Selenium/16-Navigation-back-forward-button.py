#!/usr/bin/python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")

try:
    l=driver.find_element_by_link_text("Gmail")
    sleep(2)
    l.click()
    sleep(2)
    driver.back()
    sleep(2)
    driver.forward()
    sleep(2)
except:
    pass

driver.close()