from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def backpack(self):
        backpack = self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        backpack.click()

    def bay(self):
        t_shirt = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
        t_shirt = self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
        t_shirt.click()

        onesie = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")))
        onesie = self.driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
        onesie.click()

        basket = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, "#shopping_cart_container"))
            )
        basket = self.driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container")
        basket.click()
