import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator):
        self.find_element(locator).click()

    def send_keys_to_input(self, locator, keys):
        self.find_element(locator).send_keys(keys)
        
    def get_value_input(self, locator):
        return self.find_element(locator).get_attribute('value')

    def wait_element_to_be_cliackable_and_click(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def wait_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    
    def wait_element_to_be_hidden(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))

    def get_text(self, locator):
        return self.find_element(locator).text
    
    def check_current_url(self, url):
        assert self.driver.current_url == url

    def wait_change_value(self, locator, value):
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(locator, value))

    