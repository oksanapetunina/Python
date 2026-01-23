from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class MakingAnOrder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить форму заказа")
    def say_name(self, firstName, lastName, postalCode):
        with allure.step("ввод имени"):
            """
                Ввод имени.

                :param first_name: имя.
                :type first_name: str
                :return: None
            """
            self.driver.find_element(
                By.CSS_SELECTOR, '[data-test="firstName"]').send_keys(firstName)
        with allure.step("ввод фамилии"):
            """
                        Ввод фамилии.
                        :param last_name: фамилия.
                        :type last_name: str
                        :return: None
            """
            self.driver.find_element(
                By.CSS_SELECTOR, '[data-test="lastName"]').send_keys(lastName)
        with allure.step("ввод почтового кода"):
            """
                                Ввод почтового кода.
                                :postal_code: почтовый код
                                :type postal_code: str
                                :return: None
           """
            self.driver.find_element(
                By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys(postalCode)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Проверка итоговой стоимости")
    def go_to_card(self):
        with allure.step("Получение итоговой суммы"):
            total = self.driver.find_element(
                By.CSS_SELECTOR, ".summary_total_label").text
            total_prise = float(total.split("$")[1])
            print(total_prise)

            assert total_prise == 58.29
