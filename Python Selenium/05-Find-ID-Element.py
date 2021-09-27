#!/usr/bin/python3

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")

try:
    ide = driver.find_elements_by_xpath("//*[@id]")
    for idt in ide:
        print(idt.get_attribute('id'))

except Exception as arr:
    print("Not Found It")

driver.close()