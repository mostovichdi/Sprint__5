import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from locators import RegistrationPage
from test_check_registration import TestRegistration


@pytest.fixture
def driver()-> webdriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
    # driver.quit()
