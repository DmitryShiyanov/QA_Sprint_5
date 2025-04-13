from selenium.webdriver.support.wait import WebDriverWait
from data import Constants
from locators import MainLocators
from selenium.webdriver.support import expected_conditions

class TestConstructor:

    def test_navigate_to_span_filling_active_success(self,chrome):
        chrome.get(Constants.MAIN_URL)
        elem = chrome.find_element(*MainLocators.FILLINGS_BUTTON)
        elem.click()
        active_clas = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect'
        WebDriverWait(chrome, 5).until(
            expected_conditions.visibility_of_element_located(MainLocators.MEAT_MOLUSKIN))
        assert active_clas in elem.get_attribute('class')

    def test_navigate_to_span_sauces_active_success(self,chrome):
        chrome.get(Constants.MAIN_URL)
        sauce = chrome.find_element(*MainLocators.SAUCES_BUTTON)
        sauce.click()
        active_class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        WebDriverWait(chrome, 5).until(
            expected_conditions.visibility_of_element_located(MainLocators.SAUCE_SPICYX))
        assert active_class in sauce.get_attribute('class')
    #
    def test_navigate_to_span_buns_active_success(self,chrome):
        chrome.get(Constants.MAIN_URL)
        chrome.find_element(*MainLocators.SAUCES_BUTTON).click()
        bun = chrome.find_element(*MainLocators.BUN_BUTTON)
        bun.click()
        active = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
        WebDriverWait(chrome, 5).until(
            expected_conditions.visibility_of_element_located(MainLocators.BUN_CRATOR))
        assert active in bun.get_attribute('class')
