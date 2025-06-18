import pytest
from locators.locators import CommonLocators, RegistrationLocators
from utils.generate_email import generate_email

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

        email = generate_email()
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        assert driver.find_element(*CommonLocators.USER_NAME).is_displayed()

    def test_invalid_email_registration(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("invalid-email")
        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        assert "Ошибка" in driver.find_element(*RegistrationLocators.ERROR_MESSAGE).text

    def test_existing_user_registration(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*RegistrationLocators.NO_ACCOUNT_BUTTON).click()

        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("existing@example.com")
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.REPEAT_PASSWORD_INPUT).send_keys("Test1234")
        driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

        assert "Ошибка" in driver.find_element(*RegistrationLocators.ERROR_MESSAGE).text
