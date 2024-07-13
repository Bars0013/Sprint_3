import pytest
from data import Person
from locators import MainPageLocators, AuthPageLocators, RegistrationPageLocators, RecoverPageLocators
from urls import URLS
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    def test_login_in_login_btn_success(self, driver):
        """Вход в личный кабинет через кнопку 'Войти в аккаунт' на главной странице"""
        driver = driver
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_ACCOUNT_BTN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        order_btn = driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_personal_account_btn_success(self, driver):
        """Вход в личный кабинет через кнопку 'Личный кабинет' на главной странице"""
        driver = driver
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_ACCOUNT_BTN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        order_btn = driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_registration_form_success(self, driver):
        """Вход в личный кабинет через форму регистрации"""
        driver = driver
        driver.get(URLS.REG_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.LOGIN_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_ACCOUNT_BTN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        order_btn = driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

    def test_login_in_recover_form_success(self, driver):
        """Вход в личный кабинет через форму восстановления"""
        driver = driver
        driver.get(URLS.RECOVER_PAGE_URL)
        driver.find_element(*RecoverPageLocators.LOGIN_ACCOUNT_BTN).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.LOGIN_ACCOUNT_BTN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        order_btn = driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).text

        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')

