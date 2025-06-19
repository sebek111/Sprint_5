from selenium.webdriver.common.by import By

class CommonLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    USER_NAME = (By.XPATH, "//span[text()='User']")
    PLACE_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    MODAL_AUTH_HEADER = (By.XPATH, "//h2[text()='Чтобы разместить объявление, авторизуйтесь']")

class RegistrationLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REPEAT_PASSWORD_INPUT = (By.NAME, "confirmPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'Ошибка')]")

class LoginLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

class CreateAdLocators:
    TITLE_INPUT = (By.NAME, "title")
    DESCRIPTION_INPUT = (By.NAME, "description")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")
    CONDITION_NEW = (By.XPATH, "//input[@type='radio' and @value='new']")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")
    CREATED_AD = (By.XPATH, "//div[contains(@class, 'ad-card')]")
