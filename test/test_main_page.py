import pytest
import allure
from page.main import MainPage


def test_light_off(driver):
    MainPage.navigate_to(driver, url=MainPage.BASE_URL)
    MainPage.switch_light(driver)

