from page.base import Base
from locator.main_page import MainPageLocators
import allure


class MainPage(Base):
    BASE_URL = "https://slothman.dev/"

    def switch_light(self):
        self.get_element(MainPageLocators.LIGHT_SWITCH).click()
