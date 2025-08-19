from selenium import webdriver
# import sys
# sys.path.append('C:\\Users\Matros\.vscode\Sprint_5')
from locators import RegistrationPage
import urls as urls
from generation_login import GenerationEmailPassword
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time



class TestRegistration():
    
    def test_check_registrtation_with_correct_email_password(self, driver: webdriver):
       generator = GenerationEmailPassword()
       email = generator.generate_email()
       password = generator.generate_password()
       name = generator.generate_name()

       driver.get(urls.registration_page)
    #    assert driver.current_url == urls.registration_page
       driver.find_element(*RegistrationPage.input_name_form_registration).send_keys(name)
       driver.find_element(*RegistrationPage.input_email_form_registration).send_keys(email)
       driver.find_element(*RegistrationPage.input_password_form_registration).send_keys(password)
       driver.find_element(*RegistrationPage.button_registration).click()
       WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
       
       assert urls.login_page == driver.current_url

            