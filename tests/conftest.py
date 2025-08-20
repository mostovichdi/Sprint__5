import pytest
from selenium import webdriver

# import selenium
# import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from locators import RegistrationPage
from data import DataToLogin


@pytest.fixture
def driver() -> webdriver.Chrome: # type: ignore
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
