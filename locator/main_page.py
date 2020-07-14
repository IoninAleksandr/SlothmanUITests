from selenium.webdriver.common.by import By


class MainPageLocators:
    TITLE_MESSAGE = (By.XPATH, "//h1[@class = 's-title']")
    LIGHT_SWITCH = (By.XPATH, "//div[@class='right-part']//*[local-name()='svg']")