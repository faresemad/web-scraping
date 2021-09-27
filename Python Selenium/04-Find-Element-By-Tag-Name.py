#!/usr/bin/python3

from selenium import webdriver
driver = webdriver.Firefox()
#https://www.google.com
driver.get("https://www.google.com")

try:
    driver.find_element_by_tag_name("form")
    print("Found")
except Exception as err:
    print("Not Found")

driver.close()