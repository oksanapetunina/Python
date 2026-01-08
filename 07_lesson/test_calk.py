import pytest
from selenium import webdriver
from calk_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()


def test_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.delay_input()
    calc_page.button_input()
    calc_page.get_result()
    result = calc_page.get_result()
    assert result == '15'
