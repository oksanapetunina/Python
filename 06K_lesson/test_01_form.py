from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


def test_fill_form():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'first-name'))
    )
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
