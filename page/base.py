from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
import allure


class Base:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        with allure.step(f"Переход на '{url}'"):
            self.driver.get(url)

    def get_element(self, locator, timeout=15):
        with allure.step(f"Ищу элемент '{locator}'"):
            return WebDriverWait(self.driver, timeout).until(
                ex_cond.visibility_of_element_located(locator), message=f"Can't click element by locator{locator}"
            )

    def get_elements(self, locator, timeout=15):
        with allure.step(f"Ищу элементы '{locator}'"):
            return WebDriverWait(self.driver, timeout).until(
                ex_cond.visibility_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}"
            )
