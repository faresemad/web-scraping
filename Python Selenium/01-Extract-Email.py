#!/usr/bin/python3

#import selenium , re modules
from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get("http://www.airindia.in/contact-details.htm")

#doc is the variable ,container for page source
doc = driver.page_source

#emails is container for doc 
#regex extarct email
emails = re.findall(r'[\w\.-]+@[\w\.-]+',doc)
for email in emails:
    print(email)

driver.close()