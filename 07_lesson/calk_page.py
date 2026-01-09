from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.result = (By.ID, "result")

    def delay_input(self, value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(value)
        
    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//button[contains(text(),'{button_text}')]")
        button.click()
        
    def get_result(self):
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(EC.text_to_be_present_in_element(
            By.CSS_SELECTOR, ".screen"))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
