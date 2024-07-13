import pytest
from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestProfileArea:

    def test_transition_to_pesonal_area_from_main_page_success(self, driver, get_login_driver):
        """Проверка перехода в личный кабинет с главной страницы по кнопке 'Личный кабинет' """
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BTN))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.EXIT_BTN))
        save_btn_displayed = driver.find_element(*PersonalAreaLocators.SAVE_BTN).is_displayed()

        assert driver.current_url == URLS.PROFILE_PAGE_URL and save_btn_displayed

    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, driver,
                                                                                           get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по клику на кнопку 'Конструктор' """
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BTN))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.EXIT_BTN))
        driver.find_element(*PersonalAreaLocators.CONSTRUCTOR_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUN))
        bun_displayed = driver.find_element(*MainPageLocators.BUN).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed

    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, driver, get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по клику на 'Логотип' """
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BTN))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.EXIT_BTN))
        driver.find_element(*PersonalAreaLocators.LOGO_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.BUN))
        bun_displayed = driver.find_element(*MainPageLocators.BUN).is_displayed()

        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed

    def test_logout_from_personal_area_success(self, driver, get_login_driver):
        """Проверка выхода из личного кабинета"""
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BTN))
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.EXIT_BTN))
        driver.find_element(*PersonalAreaLocators.EXIT_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_ACCOUNT_BTN))
        login_btn_displayed = driver.find_element(*AuthPageLocators.LOGIN_ACCOUNT_BTN).is_displayed()

        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed