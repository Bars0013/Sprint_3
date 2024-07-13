import pytest
from conftest import driver
from locators import MainPageLocators
from urls import URLS
from selenium import webdriver


class TestConstructorPage:
    def test_transition_to_bun_success(self, driver):
        """Проверка перехода к разделу 'Булки' """
        driver = driver
        driver.get(URLS.MAIN_PAGE_URL)
        bun = driver.find_element(*MainPageLocators.BUN).text
        bun_displayed = driver.find_element(*MainPageLocators.BUN_UL).is_displayed()

        assert bun == 'Булки' and bun_displayed


    def test_transition_to_topping_success(self, driver):
        """Проверка перехода к разделу 'Начинки' """
        driver = driver
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.TOPPINGS_BTN).click()
        topping = driver.find_element(*MainPageLocators.TOPPING).text
        topping_displayed = driver.find_element(*MainPageLocators.TOPPING_UL).is_displayed()

        assert topping == 'Начинки' and topping_displayed


    def test_transition_to_sauces_success(self, driver):
        """Проверка перехода к разделу 'Соусы' """
        driver = driver
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.SAUCES_BTN).click()
        souces = driver.find_element(*MainPageLocators.SAUCES).text
        souces_displayed = driver.find_element(*MainPageLocators.SAUCES_UL).is_displayed()

        assert souces == 'Соусы' and souces_displayed