from locators.locators import CommonLocators, LoginLocators

BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"

def test_logout_user(driver):
    driver.get(BASE_URL)
    driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON).click()

    driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys("existing@example.com")
    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys("Test1234")
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()

    driver.find_element(*CommonLocators.LOGOUT_BUTTON).click()
    assert driver.find_element(*CommonLocators.LOGIN_REGISTER_BUTTON).is_displayed()
