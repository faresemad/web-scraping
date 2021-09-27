#!/usr/bin/python3
from time import sleep
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.execute_script("window.alert('Fares Emad');")
sleep(2)
driver.close()