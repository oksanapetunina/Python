import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture

def test_shop():
    driver = webdriver.Firefox(
        service=FireFoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.CSS_SELECTOR, 'user-name').\
        send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")

    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    backpack = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
    backpack = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    backpack.click

    t_shirt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")))
    t_shirt = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    t_shirt.click

    onesie = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")))
    onesie = driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    onesie.click

    basket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#shopping_cart_container")))
    basket = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container")
    basket.click

    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, 'firstName').send_keys("Oxana")
    driver.find_element(By.CSS_SELECTOR, '#lastName').send_keys("Petunina")
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("614051")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total = driver.find_element(By.CSS_SELECTOR, "#summary_total_label").text
    total_prise = float(total.split("$")[1])
    print(total_prise)

    assert total_prise == 58.29

    driver.find_element
