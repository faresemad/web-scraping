#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.wikipedia.org/")
elm = driver.find_element_by_tag_name("html")
sleep(2)
elm.send_keys(Keys.END)
sleep(2)
elm.send_keys(Keys.HOME)
sleep(2)
driver.close()