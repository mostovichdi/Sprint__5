from selenium.webdriver.common.by import By

class RegistrationPage():
    input_name_form_registration = (By.XPATH, ".//fieldset[1]//input")
    input_email_form_registration = (By.XPATH, ".//fieldset[2]//input") 
    input_password_form_registration = (By.XPATH, ".//fieldset[3]//input") 
    button_registration = (By.XPATH, ".//button[text()='Зарегистрироваться']")