import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from card_page import CardPage
from login_page import LoginPage
from making_an_order import MakingAnOrder
from checout_page import ChecoutPage
import allure


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(6)
    WebDriverWait(driver, 10)
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()

@allure.title("Тест онлайн-магазина")
@allure.description("Переход на страницу магазина, авторизация, выбор товаров, расчёт итоговой цены")
@allure.feature("READ")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):

    """
            Авторизация
    """
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    """
            Добавление товаров в корзину
    """

    card_page = CardPage(driver)
    card_page.backpack()
    card_page.bay()

    """
            Нажатие на кнопку
    """

    checout_page = ChecoutPage(driver)
    checout_page.checkout()

    """
            Заполнение формы данными
    """

    making_an_order = MakingAnOrder(driver)
    making_an_order.say_name("Oxana", "Petunina", "614051")
    making_an_order.go_to_card()