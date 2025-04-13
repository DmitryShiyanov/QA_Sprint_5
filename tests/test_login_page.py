from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from locators import MainLocators
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class TestLoginCase:


    def test_login_on_start_page_success(self, chrome, login):
        try:
            WebDriverWait(chrome, 5).until(
                expected_conditions.presence_of_element_located(MainLocators.ORDER_BUTTON))
            assert True
        except TimeoutException:
            assert False

    def test_login_on_LK_page_success(self, chrome):
        chrome.get(Constants.MAIN_URL)
        chrome.find_element(*MainLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chrome, 3).until(
            expected_conditions.element_to_be_clickable(MainLocators.LOGIN_BUTTON))
        chrome.find_element(*MainLocators.EMAIL_FIELD).send_keys(Constants.DEF_MAIL)
        chrome.find_element(*MainLocators.PASSWORD_FIELD).send_keys(Constants.DEF_PASSWORD)
        chrome.find_element(*MainLocators.LOGIN_BUTTON).click()
        chrome.find_element(*MainLocators.PERSONAL_ACCOUNT_BUTTON).click()
        try:
            WebDriverWait(chrome, 5).until(
                expected_conditions.presence_of_element_located(MainLocators.PROFILE_BUTTON))
            assert True
        except TimeoutException:
            assert False

    def test_login_on_registration_page_success(self,chrome):
        chrome.get(Constants.MAIN_URL)
        chrome.find_element(*MainLocators.LOGIN_ACCOUNT_BUTTON).click()
        chrome.find_element(*MainLocators.REGISTRATION_HREF).click()
        chrome.find_element(*MainLocators.REGISTRATION_LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(
            expected_conditions.element_to_be_clickable(MainLocators.LOGIN_BUTTON))
        chrome.find_element(*MainLocators.EMAIL_FIELD).send_keys(Constants.DEF_MAIL)
        chrome.find_element(*MainLocators.PASSWORD_FIELD).send_keys(Constants.DEF_PASSWORD)
        chrome.find_element(*MainLocators.LOGIN_BUTTON).click()
        try:
            WebDriverWait(chrome, 5).until(
                expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))
            assert True
        except TimeoutException:
            assert False

    def test_login_on_recovery_password_page_success(self,chrome):
        chrome.get(Constants.MAIN_URL)
        chrome.find_element(*MainLocators.LOGIN_ACCOUNT_BUTTON).click()
        chrome.find_element(*MainLocators.PASSWORD_RECOVERY_BTN).click()
        chrome.find_element(*MainLocators.REGISTRATION_LOGIN_BUTTON).click()
        WebDriverWait(chrome, 3).until(
            expected_conditions.element_to_be_clickable(MainLocators.LOGIN_BUTTON))
        chrome.find_element(*MainLocators.EMAIL_FIELD).send_keys(Constants.DEF_MAIL)
        chrome.find_element(*MainLocators.PASSWORD_FIELD).send_keys(Constants.DEF_PASSWORD)
        chrome.find_element(*MainLocators.LOGIN_BUTTON).click()
        try:
            WebDriverWait(chrome, 5).until(
                expected_conditions.visibility_of_element_located(MainLocators.ORDER_BUTTON))
            assert True
        except TimeoutException:
            assert False
