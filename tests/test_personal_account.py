from selenium.webdriver.support.wait import WebDriverWait
from locators import MainLocators
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class TestAccount:

    def test_profile_entry_success(self, chrome, login):
        chrome.find_element(*MainLocators.PERSONAL_ACCOUNT_BUTTON).click()
        try:
            WebDriverWait(chrome, 5).until(
                expected_conditions.presence_of_element_located(MainLocators.PROFILE_BUTTON))
            assert True
        except TimeoutException:
            assert False

    def test_profile_exit_lk_success(self, chrome, login):
        chrome.find_element(*MainLocators.PERSONAL_ACCOUNT_BUTTON).click()
        chrome.find_element(*MainLocators.EXIT_BUTTON).click()
        try:
            WebDriverWait(chrome, 5).until(
                expected_conditions.presence_of_element_located(MainLocators.ENTER_TEXT))
            assert True
        except TimeoutException:
            assert False

    def test_navigate_from_lk_to_constructor_success(self, chrome, login):
        chrome.find_element(*MainLocators.PERSONAL_ACCOUNT_BUTTON).click()
        chrome.find_element(*MainLocators.CONSTRUCTOR_BUTTON).click()
        assert chrome.find_element(*MainLocators.BURGER_TEXT).text == 'Соберите бургер'

    def test_navigate_to_logo_stellar_burgers_success(self,chrome, login):
        chrome.find_element(*MainLocators.PERSONAL_ACCOUNT_BUTTON).click()
        chrome.find_element(*MainLocators.STELLAR_BURGERS_BTN).click()
        WebDriverWait(chrome, 5).until(
            expected_conditions.presence_of_element_located(MainLocators.BURGER_TEXT))
        assert chrome.find_element(*MainLocators.BURGER_TEXT).text == 'Соберите бургер'

