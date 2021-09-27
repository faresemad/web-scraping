#!/usr/bin/python3
from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get("URL")

doc = driver.page_source

phones = re.findall(r'' , doc)

for phone in phones:
    print(phone)

driver.close()