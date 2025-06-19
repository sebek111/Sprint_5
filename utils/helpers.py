from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import CommonLocators, LoginLocators
from data.urls import BASE_URL

def login(driver, email, password):
    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(CommonLocators.LOGIN_REGISTER_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
    ).send_keys(email)

    driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginLocators.SUBMIT_BUTTON).click()
