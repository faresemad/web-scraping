#!/usr/bin/python3
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.google.com")
cookie = {"fruit": 'mango', "chocalete": 'milk'}
driver.add_cookie(cookie)

print(driver.get_cookies())
