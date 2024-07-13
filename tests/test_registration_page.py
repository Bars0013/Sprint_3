import pytest
from data import Person, RandomData
from locators import RegistrationPageLocators, AuthPageLocators
from urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestRegistrationPage:

    def test_registration_success(self, driver):
        """Проверка регистрации пользователя"""
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BTN))
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(RandomData.password)
        driver.find_element(*RegistrationPageLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_ACCOUNT_BTN))
        login_btn_displayed = driver.find_element(*AuthPageLocators.LOGIN_ACCOUNT_BTN).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed

    def test_registration_incorrect_password_check_error(self, driver):
        """Проверка регистрации пользователя с некорректным паролем (менее 6 символов)"""
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BTN))
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(12345)
        driver.find_element(*RegistrationPageLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_any_elements_located(RegistrationPageLocators.ERROR_MESSAGE_INCORRECT_PASSWORD))
        error = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE_INCORRECT_PASSWORD).text

        assert (error == 'Некорректный пароль') and (driver.current_url == URLS.REG_PAGE_URL)

    def test_double_registration_check_error(self, driver):
        """Проверка повторной регистрации пользователя"""
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.REGISTRATION_BTN))
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*RegistrationPageLocators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE_DOUBLE_REG))
        error = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE_DOUBLE_REG).text

        assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REG_PAGE_URL)

