from selenium import webdriver
from data import ExpectedText
from locators import LoginPage, MainPage, RegistrationPage, ForgotPasswordPage
import urls as urls
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

    def test_check_constructor_from_sauces_to_bread(self, driver: webdriver.Chrome):

        driver.get(urls.main_page)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                MainPage.button_entrance_in_account_to_login
            )
        )
        driver.find_element(*MainPage.button_sauces).click()
        driver.find_element(*MainPage.button_bread).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.button_bread_selected)
        )
        text_section_bread = driver.find_element(
            *MainPage.text_bread_form_ingredients
        ).text
        assert text_section_bread == ExpectedText.BREAD

    def test_check_constructor_from_bread_to_sauces(self, driver: webdriver.Chrome):

        driver.get(urls.main_page)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                MainPage.button_entrance_in_account_to_login
            )
        )
        driver.find_element(*MainPage.button_sauces).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.button_sauces_selected)
        )
        text_section_sauces = driver.find_element(
            *MainPage.text_sauces_form_ingredients
        ).text
        assert text_section_sauces == ExpectedText.SAUCES

    def test_check_constructor_from_bread_to_fillings(self, driver: webdriver.Chrome):

        driver.get(urls.main_page)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                MainPage.button_entrance_in_account_to_login
            )
        )
        driver.find_element(*MainPage.button_fillings).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPage.button_fillings_selected)
        )
        text_section_fillings = driver.find_element(
            *MainPage.text_fillings_form_ingredients
        ).text
        assert text_section_fillings == ExpectedText.FILLINGS
