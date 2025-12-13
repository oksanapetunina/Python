from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServise
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeServise(ChromeDriverManager().install())
)
driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
clic_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))
    )
clic_button.click()

content = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()
