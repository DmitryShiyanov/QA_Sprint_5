import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from locators import MainLocators
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class TestRegistration:


    def test_create_account_with_long_pass_success(self, chrome):
        chrome.get(Constants.MAIN_URL)
        chrome.find_element(*MainLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome, 3).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))
        chrome.find_element(*MainLocators.REGISTRATION_HREF).click()
        chrome.find_element(*MainLocators.NAME_FIELD).send_keys(Constants.NAME)
        chrome.find_element(*MainLocators.EMAIL_FIELD).send_keys(Constants.RANDOM_MAIL)
        chrome.find_element(*MainLocators.PASSWORD_FIELD).send_keys(Constants.RANDOM_PASS)
        chrome.find_element(*MainLocators.REGISTRATION_BUTTON).click()
        try:
            WebDriverWait(chrome, 5).until(
                expected_conditions.presence_of_element_located(MainLocators.ENTER_TEXT))
            assert True
        except TimeoutException:
            assert False

    @pytest.mark.parametrize('password', [' ', 1, 123, 12345])
    def test_create_account_with_short_pass_failure(self, chrome, password):
        chrome.get(Constants.MAIN_URL)
        chrome.find_element(*MainLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome, 3).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))
        chrome.find_element(*MainLocators.REGISTRATION_HREF).click()
        chrome.find_element(*MainLocators.NAME_FIELD).send_keys(Constants.NAME)
        chrome.find_element(*MainLocators.EMAIL_FIELD).send_keys(Constants.RANDOM_MAIL)
        chrome.find_element(*MainLocators.PASSWORD_FIELD).send_keys(password)
        chrome.find_element(*MainLocators.REGISTRATION_BUTTON).click()
        assert chrome.find_element(*MainLocators.ERROR_TEXT).text == 'Некорректный пароль'
