#!/usr/bin/python3
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.google.com')
try:
    driver.find_elements_by_xpath('//a[@class="pR49Ae gsfi"]')
    print("Found It")
except Exception as err:
    print("Not Found")
driver.close()