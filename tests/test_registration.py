from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import BASE_URL
from data.users import TEST_USER_EMAIL
from locators.locators import CommonLocators, RegistrationLocators
from utils.generate_email import generate_email

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)
        ).click()

        email = generate_email()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.EMAIL_INPUT)
        ).send_keys(email)

        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        user_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CommonLocators.USER_NAME)
        )
        assert user_name.is_displayed()

    def test_invalid_email_registration(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.EMAIL_INPUT)
        ).send_keys("invalidemail")

        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.ERROR_MESSAGE)
        )
        assert "Ошибка" in error.text

    def test_existing_user_registration(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.EMAIL_INPUT)
        ).send_keys(TEST_USER_EMAIL)

        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationLocators.ERROR_MESSAGE)
        )
        assert "Ошибка" in error.text
