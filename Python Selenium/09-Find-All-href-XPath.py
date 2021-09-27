#!/usr/bin/python3
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.google.com")
try:
    ids=driver.find_elements_by_xpath('//*[@href]')
    for i in ids:
        print(i.get_attribute('href'))
except Exception as err:
    print('Not Found')
driver.close()