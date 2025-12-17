import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture

def test_fill_form():
    driver = webdriver.Edge(service=(EdgeChromiumDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.ID, 'first-name').send_keys("Иван")
    driver.find_element(By.ID, 'last-name').send_keys("Петров")
    driver.find_element(By.ID, 'address').send_keys("Ленина, 55-3")
    driver.find_element(By.ID, 'e-mail').send_keys("test@skypro.com")
    driver.find_element(By.ID, 'phone').send_keys("+7985899998787")
    driver.find_element(By.ID, 'zip-code').send_keys("")
    driver.find_element(By.ID, 'city').send_keys("Москва")
    driver.find_element(By.ID, 'country').send_keys("Россия")
    driver.find_element(By.ID, 'job-position').send_keys("QA")
    driver.find_element(By.ID, 'company').send_keys("SkyPro")

    driver.find_element(By.ID, 'submit-button').click()

    zip_code_field = driver.find_element(By.ID, 'zip-code')
    assert "error" in zip_code_field.get_attribute(
        "class"), "Поле Zip code не подсвечено красным"

    fields = driver.find_elements(By.CSS_SELECTOR, "input")
    for field in fields:
        if field != zip_code_field:
            assert "success" in field.get_attribute("class"), \
                f"Поле {field.get_attribute('name')} не подсвечено зеленым"

    driver.quit()
