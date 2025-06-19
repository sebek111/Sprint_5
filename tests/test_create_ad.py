from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import CommonLocators, CreateAdLocators
from utils.helpers import login
from data.urls import BASE_URL
from data.users import TEST_USER_EMAIL, TEST_USER_PASSWORD

class TestCreateAd:

    def test_create_ad_unauthorized(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.PLACE_AD_BUTTON)
        ).click()

        modal_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CommonLocators.MODAL_AUTH_HEADER)
        )
        assert modal_header.is_displayed()

    def test_create_ad_authorized(self, driver):
        login(driver, TEST_USER_EMAIL, TEST_USER_PASSWORD)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(CommonLocators.PLACE_AD_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CreateAdLocators.TITLE_INPUT)
        ).send_keys("Телефон")

        driver.find_element(*CreateAdLocators.DESCRIPTION_INPUT).send_keys("Продам смартфон")
        driver.find_element(*CreateAdLocators.PRICE_INPUT).send_keys("10000")
        driver.find_element(*CreateAdLocators.CATEGORY_DROPDOWN).send_keys("Электроника")
        driver.find_element(*CreateAdLocators.CITY_DROPDOWN).send_keys("Москва")
        driver.find_element(*CreateAdLocators.CONDITION_NEW).click()
        driver.find_element(*CreateAdLocators.SUBMIT_BUTTON).click()

        created_ad = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CreateAdLocators.CREATED_AD)
        )
        assert created_ad.is_displayed()

