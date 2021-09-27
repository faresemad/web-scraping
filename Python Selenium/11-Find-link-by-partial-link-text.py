#!/usr/bin/python3
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://ar.wikipedia.org")
try:
    driver.find_elements_by_partial_link_text("Terms")
    print("Found It")
except Exception as err:
    print("Not Found")
driver.close()