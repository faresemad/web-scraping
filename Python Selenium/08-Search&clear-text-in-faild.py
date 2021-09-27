import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")

search = driver.find_elements_by_id("1st-id")
search.send_keys('python3')
search.send_keys(Keys.RETURN)
time.sleep(5)
search.clear()
time.sleep(5)
driver.close()