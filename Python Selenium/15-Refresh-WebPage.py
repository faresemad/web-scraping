#!/usr/bin/python3
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")

sleep(2)
driver.refresh()
sleep(3)
driver.close()