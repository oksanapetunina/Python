import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from card_page import CardPage
from login_page import LoginPage
from making_an_order import MakingAnOrder
from checout_page import ChecoutPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(6)
    WebDriverWait(driver, 10)
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    card_page = CardPage(driver)
    card_page.backpack()
    card_page.bay()

    checout_page = ChecoutPage(driver)
    checout_page.checkout()

    making_an_order = MakingAnOrder(driver)
    making_an_order.say_name("Oxana", "Petunina", "614051")
    making_an_order.go_to_card()
