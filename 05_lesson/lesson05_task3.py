from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/inputs")


search_field = driver.find_element(By.CSS_SELECTOR, 'input')
search_field.send_keys("Sky")

sleep(3)
search_field.clear()

search_field.send_keys("Pro")

driver.quit()

sleep(3)
