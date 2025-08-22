from selenium import webdriver
from data import DataToLogin
from locators import RegistrationPage
import urls as urls
from generation_login import GenerationEmailPassword
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_check_registrtation_with_correct_email_password(
        self, driver: webdriver.Chrome
    ):
        generator = GenerationEmailPassword()
        email = generator.generate_email()
        password = generator.generate_password()
        name = generator.generate_name()

        driver.get(urls.registration_page)
        driver.find_element(*RegistrationPage.input_name_form_registration).clear()
        driver.find_element(*RegistrationPage.input_name_form_registration).send_keys(
            name
        )
        driver.find_element(*RegistrationPage.input_email_form_registration).clear()
        driver.find_element(*RegistrationPage.input_email_form_registration).send_keys(
            email
        )
        driver.find_element(*RegistrationPage.input_password_form_registration).clear()
        driver.find_element(
            *RegistrationPage.input_password_form_registration
        ).send_keys(password)
        driver.find_element(*RegistrationPage.button_registration).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
        assert urls.login_page == driver.current_url

    def test_check_registration_with_empty_name(self, driver: webdriver):
        generator = GenerationEmailPassword()
        email = generator.generate_email()
        password = generator.generate_password()

        driver.get(urls.registration_page)
        driver.find_element(*RegistrationPage.input_email_form_registration).clear()
        driver.find_element(*RegistrationPage.input_email_form_registration).send_keys(
            email
        )
        driver.find_element(*RegistrationPage.input_password_form_registration).clear()
        driver.find_element(
            *RegistrationPage.input_password_form_registration
        ).send_keys(password)
        driver.find_element(*RegistrationPage.button_registration).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.registration_page))
        assert urls.login_page != driver.current_url

    def test_check_registration_with_incorrect_password(self, driver: webdriver):
        generator = GenerationEmailPassword()
        email = generator.generate_email()
        password = "12345"
        name = generator.generate_name()

        driver.get(urls.registration_page)
        driver.find_element(*RegistrationPage.input_name_form_registration).clear()
        driver.find_element(*RegistrationPage.input_name_form_registration).send_keys(
            name
        )
        driver.find_element(*RegistrationPage.input_email_form_registration).clear()
        driver.find_element(*RegistrationPage.input_email_form_registration).send_keys(
            email
        )
        driver.find_element(*RegistrationPage.input_password_form_registration).clear()
        driver.find_element(
            *RegistrationPage.input_password_form_registration
        ).send_keys(password)
        driver.find_element(*RegistrationPage.button_registration).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((RegistrationPage.text_incorrect_password))
        )
        assert urls.login_page != driver.current_url

    def test_check_impossible_registration_with_exsist_user(self, driver: webdriver):
        email = DataToLogin.NAME
        password = DataToLogin.EMAIL
        name = DataToLogin.PASSWORD

        driver.get(urls.registration_page)
        driver.find_element(*RegistrationPage.input_name_form_registration).clear()
        driver.find_element(*RegistrationPage.input_name_form_registration).send_keys(
            name
        )
        driver.find_element(*RegistrationPage.input_email_form_registration).clear()
        driver.find_element(*RegistrationPage.input_email_form_registration).send_keys(
            email
        )
        driver.find_element(*RegistrationPage.input_password_form_registration).clear()
        driver.find_element(
            *RegistrationPage.input_password_form_registration
        ).send_keys(password)
        driver.find_element(*RegistrationPage.button_registration).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPage.text_existed_user)
        )
        assert urls.login_page != driver.current_url
