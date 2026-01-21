from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure

class ChecoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):
        with allure.step("нажатие на кнопку"):
            self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()