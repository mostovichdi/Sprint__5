from selenium import webdriver
from data import DataToLogin
from locators import (
    AccoutProfilePage,
    LoginPage,
    MainPage,
    RegistrationPage,
    ForgotPasswordPage,
)
import urls as urls
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAccountToConstructor:

    def test_check_go_from_account_profile_to_constructor_by_button_constructor(
        self, driver: webdriver.Chrome
    ):
        email = DataToLogin.EMAIL
        password = DataToLogin.PASSWORD
        driver.get(urls.login_page)

        WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
        driver.find_element(*LoginPage.input_email_form_login).clear()
        driver.find_element(*LoginPage.input_email_form_login).send_keys(email)
        driver.find_element(*LoginPage.input_password_form_login).clear()
        driver.find_element(*LoginPage.input_password_form_login).send_keys(password)
        driver.find_element(*LoginPage.button_login_log_page).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_place_order_in_account)
        )
        driver.find_element(*MainPage.button_account_to_login).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccoutProfilePage.button_constructor)
        )
        driver.find_element(*AccoutProfilePage.button_constructor).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.text_make_burger)
        )
        assert driver.current_url == urls.main_page

    def test_check_go_from_account_profile_to_constructor_by_button_logo(
        self, driver: webdriver.Chrome
    ):
        email = DataToLogin.EMAIL
        password = DataToLogin.PASSWORD
        driver.get(urls.login_page)

        WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
        driver.find_element(*LoginPage.input_email_form_login).clear()
        driver.find_element(*LoginPage.input_email_form_login).send_keys(email)
        driver.find_element(*LoginPage.input_password_form_login).clear()
        driver.find_element(*LoginPage.input_password_form_login).send_keys(password)
        driver.find_element(*LoginPage.button_login_log_page).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_place_order_in_account)
        )
        driver.find_element(*MainPage.button_account_to_login).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccoutProfilePage.button_logo)
        )
        driver.find_element(*AccoutProfilePage.button_logo).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.text_make_burger)
        )
        assert driver.current_url == urls.main_page
