import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.maximize_window()
    wd.implicitly_wait(3)
    yield wd
    wd.quit()