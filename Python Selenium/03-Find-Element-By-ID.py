#!/usr/bin/python3

from selenium import webdriver

driver = webdriver.Firefox()
#https://www.google.com
driver.get("https://www.google.com")

try:
    driver.find_element_by_id("gb")
    print('Found ID')

except Exception as err:
    print("Error Exception")
driver.close()