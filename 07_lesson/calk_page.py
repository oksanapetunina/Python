from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(5)
        self.result = (By.ID, "result")

    def delay_input(self):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

    def button_input(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self):
        waiter = WebDriverWait(self.driver, 45)
        waiter.until(EC.text_to_be_present_in_element(
            By.CSS_SELECTOR, ".screen"))
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text

        assert result == "15"

        self._driver.quit()
