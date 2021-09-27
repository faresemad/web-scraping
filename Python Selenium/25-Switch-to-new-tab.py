#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.google.com")
elm = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.get("https://www.facebook.com")
sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)
sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.instagram.com/farresemadd/")
# driver.execute_script('''window.open("https://www.google.com", "_blank");''')
# time.sleep(5)
# driver.quit()
