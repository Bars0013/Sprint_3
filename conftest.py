from selenium import webdriver
import pytest
from locators import MainPageLocators, AuthPageLocators
from urls import URLS
from data import Person


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
    driver.find_element(*AuthPageLocators.LOGIN_ACCOUNT_BTN).click()

    return driver