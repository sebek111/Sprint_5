from locators.locators import CommonLocators, LoginLocators, CreateAdLocators

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

def login(driver):
    driver.get(BASE_URL)
    driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON).click()
    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys("existing@example.com")
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("Test1234")
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

def test_create_ad_unauthorized(driver):
    driver.get(BASE_URL)
    driver.find_element(*CommonLocators.PLACE_AD_BUTTON).click()
    assert driver.find_element(*CommonLocators.MODAL_AUTH_HEADER).is_displayed()

def test_create_ad_authorized(driver):
    login(driver)
    driver.find_element(*CommonLocators.PLACE_AD_BUTTON).click()
    driver.find_element(*CreateAdLocators.TITLE_INPUT).send_keys("Телефон")
    driver.find_element(*CreateAdLocators.DESCRIPTION_INPUT).send_keys("Продам смартфон")
    driver.find_element(*CreateAdLocators.PRICE_INPUT).send_keys("10000")
    driver.find_element(*CreateAdLocators.CATEGORY_DROPDOWN).send_keys("Электроника")
    driver.find_element(*CreateAdLocators.CITY_DROPDOWN).send_keys("Москва")
    driver.find_element(*CreateAdLocators.CONDITION_NEW).click()
    driver.find_element(*CreateAdLocators.SUBMIT_BUTTON).click()

    assert driver.find_element(*CreateAdLocators.CREATED_AD).is_displayed()
