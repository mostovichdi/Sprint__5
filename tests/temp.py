from selenium import webdriver
# import sys
# sys.path.append('C:\\Users\Matros\.vscode\Sprint_5')
from ..locators import RegistrationPage
import urls
from generation_login import GenerationEmailPassword
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_check_registrtation_with_correct_email_password(driver):
    generator = GenerationEmailPassword()
    # email = generator.generate_email()
    # password = generator.generate_password()
    name = generator.generate_name()
    url = urls.registration_page
    print(url)

    driver.get(url)
    driver.find_element(*RegistrationPage().input_name_form_registration).send_keys(name)
  

driver = webdriver.Chrome()
driver.maximize_window()
test_check_registrtation_with_correct_email_password(driver)
    
       


       