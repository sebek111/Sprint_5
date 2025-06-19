from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.urls import BASE_URL
from data.users import TEST_USER_EMAIL, TEST_USER_PASSWORD
from locators.locators import CommonLocators, LoginLocators

class TestLogin:

    def test_login_user(self, driver):
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
        ).send_keys(TEST_USER_EMAIL)

        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
        driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

        user_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CommonLocators.USER_NAME)
        )
        assert user_name.is_displayed()
