import pytest
from selenium import webdriver


@pytest.fixture
def driver() -> webdriver.Chrome: # type: ignore
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()