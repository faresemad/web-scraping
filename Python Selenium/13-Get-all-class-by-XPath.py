#!/usr/bin/python3
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.google.com")
try:
    ids = driver.find_elements_by_xpath('//*[@class]')
    for i in ids:
        print(i.get_attribute('id'))
except Exception as err:
    print("Not Found")

driver.close()