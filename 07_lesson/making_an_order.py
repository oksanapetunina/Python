from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MakingAnOrder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def say_name(self, firstName, lastName, postalCode):
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="firstName"]').send_keys(firstName)
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="lastName"]').send_keys(lastName)
        self.driver.find_element(
            By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys(postalCode)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def go_to_card(self):
        total = self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
        total_prise = float(total.split("$")[1])
        print(total_prise)

        assert total_prise == 58.29
