from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(driver, 5)

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').\
            send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').\
            send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
