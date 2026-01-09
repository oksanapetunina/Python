import pytest
from selenium import webdriver
from calk_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.delay_input("45")
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")
    calc_page.get_result()

    result = calc_page.get_result()
    assert result == '15', f"Expected result to be '15', but got '{result}'."