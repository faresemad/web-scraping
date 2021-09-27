#!/usr/bin/python3
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.google.com")
elm = driver.find_element_by_id("1st-ib")
location = elm.location
size = elm.location
print(location)
print(size)
