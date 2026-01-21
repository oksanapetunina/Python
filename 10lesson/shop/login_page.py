from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Аутентификация пользователя")
    def login(self, username, password):
        with allure.step("ввод логина"):
            self.driver.find_element(By.CSS_SELECTOR, '#user-name').\
                send_keys(username)
        with allure.step("ввод пароля"):
            self.driver.find_element(By.CSS_SELECTOR, '#password').\
                send_keys(password)
        with allure.step("вход"):
            self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
