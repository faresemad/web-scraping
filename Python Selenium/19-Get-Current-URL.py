#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://parrotsec.org/")
driver.find_element_by_link_text("Download").click()
print(driver.current_url)
driver.close()