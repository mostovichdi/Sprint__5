from selenium import webdriver
from data import DataToLogin
from locators import LoginPage, MainPage, RegistrationPage, ForgotPasswordPage
import urls as urls
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_check_login_from_main_page_by_entrance_in_account(
        self, driver: webdriver.Chrome
    ):
        email = DataToLogin.EMAIL
        password = DataToLogin.PASSWORD
        driver.get(urls.main_page)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_entrance_in_account_to_login)
        )
        driver.find_element(*MainPage.button_entrance_in_account_to_login).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
        driver.find_element(*LoginPage.input_email_form_login).clear()
        driver.find_element(*LoginPage.input_email_form_login).send_keys(email)
        driver.find_element(*LoginPage.input_password_form_login).clear()
        driver.find_element(*LoginPage.input_password_form_login).send_keys(password)
        driver.find_element(*LoginPage.button_login_log_page).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_place_order_in_account)
        )
        text_of_order = driver.find_element(
            *MainPage.button_place_order_in_account
        ).text
        assert text_of_order == "Оформить заказ"

    def test_check_login_from_main_page_by_click_account(
        self, driver: webdriver.Chrome
    ):
        email = DataToLogin.EMAIL
        password = DataToLogin.PASSWORD
        driver.get(urls.main_page)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_account_to_login)
        )
        driver.find_element(*MainPage.button_account_to_login).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
        driver.find_element(*LoginPage.input_email_form_login).clear()
        driver.find_element(*LoginPage.input_email_form_login).send_keys(email)
        driver.find_element(*LoginPage.input_password_form_login).clear()
        driver.find_element(*LoginPage.input_password_form_login).send_keys(password)
        driver.find_element(*LoginPage.button_login_log_page).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_place_order_in_account)
        )
        text_of_order = driver.find_element(
            *MainPage.button_place_order_in_account
        ).text
        assert text_of_order == "Оформить заказ"

    def test_check_login_from_registration_page(self, driver: webdriver.Chrome):
        email = DataToLogin.EMAIL
        password = DataToLogin.PASSWORD
        driver.get(urls.registration_page)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPage.button_login_reg_page)
        )
        driver.find_element(*RegistrationPage.button_login_reg_page).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
        driver.find_element(*LoginPage.input_email_form_login).clear()
        driver.find_element(*LoginPage.input_email_form_login).send_keys(email)
        driver.find_element(*LoginPage.input_password_form_login).clear()
        driver.find_element(*LoginPage.input_password_form_login).send_keys(password)
        driver.find_element(*LoginPage.button_login_log_page).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_place_order_in_account)
        )
        text_of_order = driver.find_element(
            *MainPage.button_place_order_in_account
        ).text
        assert text_of_order == "Оформить заказ"

    def test_check_login_from_forgot_password_page(self, driver: webdriver.Chrome):
        email = DataToLogin.EMAIL
        password = DataToLogin.PASSWORD
        driver.get(urls.forgot_password_page)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPage.button_login_forgot_page)
        )
        driver.find_element(*ForgotPasswordPage.button_login_forgot_page).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(urls.login_page))
        driver.find_element(*LoginPage.input_email_form_login).clear()
        driver.find_element(*LoginPage.input_email_form_login).send_keys(email)
        driver.find_element(*LoginPage.input_password_form_login).clear()
        driver.find_element(*LoginPage.input_password_form_login).send_keys(password)
        driver.find_element(*LoginPage.button_login_log_page).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPage.button_place_order_in_account)
        )
        text_of_order = driver.find_element(
            *MainPage.button_place_order_in_account
        ).text
        assert text_of_order == "Оформить заказ"
