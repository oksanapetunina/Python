from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/login")

un = "input[name='username']"
push_login = driver.find_element(By.CSS_SELECTOR, un)
push_login.send_keys("tomsmith")

pw = "input[name='password']"
push_login = driver.find_element(By.CSS_SELECTOR, pw)
push_login.send_keys("SuperSecretPassword!")

sleep(3)

push_log = "button.radius"
push_log = driver.find_element(By.CSS_SELECTOR, push_log).click()

success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(success_message.text)

driver.quit()

sleep(3)
