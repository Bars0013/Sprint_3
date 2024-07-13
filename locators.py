from selenium.webdriver.common.by import By


class MainPageLocators:
    """Главная страница"""
    MAIN_FORM = (By.XPATH, ".//main[@class = 'App_componentContainer__2JC2W']")  # Форма главной страницы сайта
    LOGO_BTN = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка войти в аккаунт
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    ORDER_FEED_BTN = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    BUN_BTN = (By.XPATH, ".//span[text() = 'Булки']")  # Кнопка переключения на булки
    SAUCES_BTN = (By.XPATH, ".//span[text() = 'Соусы']")  # Кнопка переключения на соусы
    TOPPINGS_BTN = (By.XPATH, ".//span[text() = 'Начинки']")  # Кнопка переключения на начинки
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")  # Кнопка оформить заказ
    SAUCES = (By.XPATH, ".//h2[text() = 'Соусы']")  # Текст соусы на главной странице
    SAUCES_UL = (
    By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[2]")  # Выбор соусов на главной странице
    BUN = (By.XPATH, ".//h2[text() = 'Булки']")  # Текст булки на главной странице
    BUN_UL = (
    By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[1]")  # Выбор булок на главной странице
    TOPPING = (By.XPATH, ".//h2[text() = 'Начинки']")  # Текст начинки на главной странице
    TOPPING_UL = (
    By.XPATH, "(.//ul[@class = 'BurgerIngredients_ingredients__list__2A-mT'])[3]")  # Выбор начинок на главной странице


class AuthPageLocators:
    """Форма авторизации"""
    AUTH_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")  # Форма авторизации
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    LOGIN_ACCOUNT_BTN = (By.XPATH, "//button[text() = 'Войти']")  # Кнопка войти
    REGISTRATION_BTN = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # Кнопка зерегистрироваться
    RECOVER_BTN = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Кнопка восстановить пароль
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    ORDER_FEED_BTN = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    LOGO_BTN = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета


class RegistrationPageLocators:
    """Форма регистрации"""
    NAME_INPUT = (By.XPATH, "(.//input[@name = 'name'])[1]")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "(.//input[@name = 'name'])[2]")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    REGISTRATION_BTN = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # Кнопка зерегистрироваться
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    ORDER_FEED_BTN = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    LOGO_BTN = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета
    ERROR_MESSAGE_DOUBLE_REG = (
    By.XPATH, ".//p[text() = 'Такой пользователь уже существует']")  # Ошибка при повторной регистрации
    ERROR_MESSAGE_INCORRECT_PASSWORD = (
    By.XPATH, ".//p[text() = 'Некорректный пароль']")  # Ошибка при вводе некорректного пароля


class RecoverPageLocators:
    """Форма восстановления пароля"""
    EMAIL_INPUT = (By.XPATH, ".//label[text() = 'Email']")  # Поле ввода email
    RECOVER_BTN = (By.XPATH, ".//button[text() = 'Восстановить']")  # Кнопка восстановить
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка войти
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    ORDER_FEED_BTN = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    LOGO_BTN = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета


class PersonalAreaLocators:
    """Форма личного кабинета"""
    PROFILE_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")  # Форма личного кабинета
    PROFILE_BTN = (By.XPATH, ".//a[text() = 'Профиль']")  # Кнопка профиль
    ORDER_HISTORY_BTN = (By.XPATH, ".//a[text() = 'История заказов']")  # Кнопка история заказов
    EXIT_BTN = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выход
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")  # Кнопка сохранить
    CANSEL_BTN = (By.XPATH, ".//button[text() = 'Отмена']")  # Кнопка отмена
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text() = 'Конструктор']")  # Кнопка конструктор
    ORDER_FEED_BTN = (By.XPATH, ".//p[text() = 'Лента Заказов']")  # Кнопка лента заказов
    LOGO_BTN = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")  # Кнопка главной страницы сайта
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")  # Кнопка личного кабинета