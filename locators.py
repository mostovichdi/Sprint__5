from selenium.webdriver.common.by import By


class RegistrationPage:
    # форма ввода имени для регистрации
    input_name_form_registration = (By.XPATH, ".//fieldset[1]//input")
    # форма ввода email для регистрации
    input_email_form_registration = (By.XPATH, ".//fieldset[2]//input")
    # форма ввода пароля для регистрации
    input_password_form_registration = (By.XPATH, ".//fieldset[3]//input")
    # кнопка "Зарегистироваться"
    button_registration = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке "Некорректный пароль"
    text_incorrect_password = (By.XPATH, ".//p[text()='Некорректный пароль']")
    # Сообщение об ошибке "Такой пользователь уже существует"
    text_existed_user = (By.XPATH, ".//p[text()='Такой пользователь уже существует']")
    # Кнопка "Войти" на странице регистрации
    button_login_reg_page = (By.XPATH, ".//a[text() = 'Войти']")

class MainPage:
    # Кнопка "Войти в аккаунт" на главной странице
    button_entrance_in_account_to_login = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # Кнопка "Оформить Заказ" на главной странице после входе в аккаунт
    button_place_order_in_account = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    # Кнопка "Личный кабинет" на главной странице
    button_account_to_login = (By.XPATH, ".//a/p[text() = 'Личный Кабинет']")
    # Надпись "Собери бургер"
    text_make_burger = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
    # Кнопка "Булки" в секции ингдредиентов
    button_bread = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Булки']")
    # Кнопка "Соусы" в секции ингредиентов
    button_sauces = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Соусы']")
    # Кнопка "Начинки" в секции ингредиентов
    button_fillings = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Начинки']")
    # Кнопка "Булки" в секции ингредиентов, если выбрать раздел "Булки"
    button_bread_selected = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Булки']")
    # Кнопка "Соусы" в секции ингредиентов, если выбрать раздел "Соусы"
    button_sauces_selected = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Соусы']")
    # Кнопка "Начинки" в секции ингредиентов, если выбрать раздел "Начинки"
    button_fillings_selected = (By.XPATH, ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[text() = 'Начинки']")
    # Название раздела "Булки"
    text_bread_form_ingredients = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/h2[text() = 'Булки']")
    # Название раздела "Соусы"
    text_sauces_form_ingredients = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/h2[text() = 'Соусы']")
    # Название раздела "Начинки"
    text_fillings_form_ingredients = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']/h2[text() = 'Начинки']")
    
     


class LoginPage:
    # Форма для ввода email при входе 
    input_email_form_login = (By.XPATH, ".//fieldset[1]//input")
    # Форма для ввода пароля
    input_password_form_login = (By.XPATH, ".//fieldset[2]//input")
    # Кнопка "Войти" на странице входа в аккаунт
    button_login_log_page = (By.XPATH, ".//button[text()='Войти']")

class ForgotPasswordPage:
    # Кнопка "Войти" на странице восстановления пароля
    button_login_forgot_page = (By.XPATH, ".//a[text() = 'Войти']")

class AccoutProfilePage:
    # Кнопка "Выход" на странице профиля
    button_logout = (By.XPATH, ".//button[text() = 'Выход']")
    # Кнопка "Сохранить" на странице профиля
    button_save = (By.XPATH, ".//button[text() = 'Сохранить']")
    # Кнопка перехода на страницу Конструктора из личного кабинета через кнопку "Конструктор"
    button_constructor = (By.XPATH, ".//a/p[text() = 'Конструктор']")
    # Кнопка перехода на страницу Конструктора из личного кабинета через нажатие на логотип сайта
    button_logo = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']/a")