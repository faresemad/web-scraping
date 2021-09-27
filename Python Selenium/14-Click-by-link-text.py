#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")
elm = driver.find_element_by_link_text('Gmail')
driver.implicitly_wait(6)
elm.click()
# driver.close()