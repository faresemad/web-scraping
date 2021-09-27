#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://parrotsec.org/")
driver.set_window_size(1000, 600)
sleep(3)
driver.maximize_window()
sleep(3)
driver.minimize_window()
sleep(3)
driver.close()
