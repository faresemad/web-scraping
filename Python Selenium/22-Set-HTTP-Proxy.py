#!/usr/bin/python3
from selenium import webdriver
from time import sleep

# 179.184.224.91:3128

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "179.184.224.91")
profile.set_preference("network.proxy.http_port", 3128)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)
driver.get("http://whatismyipaddress.com")
sleep(3)
driver.close()
