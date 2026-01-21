from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calk_page import CalculatorPage
import pytest
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест калькулятора")
@allure.description("Вызов онлайн калькулятора и выполнение действий")
@allure.feature("READ")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open_page(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    with allure.step("установка задержки 45 секунд"):
        calculator_page.enter_delay_value("45")
    with allure.step("ввод числа 7"):    
        calculator_page.click_button("7")
    with allure.step("ввод знака сложение"):
        calculator_page.click_operator_button("+")
    with allure.step("ввод числа 8"):
        calculator_page.click_button("8")
    with allure.step("ввод знака равно"):
        calculator_page.click_equals_button()

    result = calculator_page.get_result_text()

    result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
    result = result_element.text.strip()

    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, "div.screen"), "15"))

    result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
    result = result_element.text.strip()
    assert result == "15"