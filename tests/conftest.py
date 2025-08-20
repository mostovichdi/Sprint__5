import pytest
from selenium import webdriver

# import selenium
# import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from locators import RegistrationPage
from data import DataToLogin


@pytest.fixture
def driver() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_user(driver):
    name = DataToLogin.NAME
    email = DataToLogin.EMAIL
    password = DataToLogin.PASSWORD
