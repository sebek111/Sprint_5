from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import login
from data.urls import BASE_URL
from data.users import TEST_USER_EMAIL, TEST_USER_PASSWORD
from locators.locators import CommonLocators

class TestLogout:

    def test_logout_user(self, driver):
        login(driver, TEST_USER_EMAIL, TEST_USER_PASSWORD)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.LOGOUT_BUTTON)
        ).click()

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CommonLocators.LOGIN_REGISTER_BUTTON)
        )
        assert login_button.is_displayed()
