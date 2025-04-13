import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Constants
from locators import MainLocators


@pytest.fixture
def chrome():
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login(chrome):
    chrome.get(Constants.MAIN_URL)
    chrome.find_element(*MainLocators.LOGIN_ACCOUNT_BUTTON).click()
    WebDriverWait(chrome, 3).until(
        expected_conditions.element_to_be_clickable(MainLocators.LOGIN_BUTTON))
    chrome.find_element(*MainLocators.EMAIL_FIELD).send_keys(Constants.DEF_MAIL)
    chrome.find_element(*MainLocators.PASSWORD_FIELD).send_keys(Constants.DEF_PASSWORD)
    chrome.find_element(*MainLocators.LOGIN_BUTTON).click()