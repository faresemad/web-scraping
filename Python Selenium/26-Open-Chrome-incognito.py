#!/usr/bin/python3
from selenium import webdriver
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')

driver = webdriver.Chrome(chrome_options=chrome_option)
driver.get("https://www.google.com")
