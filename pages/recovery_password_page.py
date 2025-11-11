import allure
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from data.data import Constants
from pages.base_page import BasePage

class RecoveryPasswordPage(BasePage):

    @allure.step('Заполняю поле email')
    def fill_email_input(self, email):
        self.send_keys_to_input(RecoveryPasswordPageLocators.email_input, email)

    @allure.step('Нажимаю на кнопку Восстановить')
    def click_recovery_button(self):
        self.click_element(RecoveryPasswordPageLocators.recovery_button)


    @allure.step('Проверяю, что появилось поле ввести код')
    def check_code_visible(self):
        assert self.wait_element_to_be_visible(RecoveryPasswordPageLocators.code_input)

    @allure.step('Ввожу пароль')
    def fill_password_input(self, password):
        self.send_keys_to_input(RecoveryPasswordPageLocators.password_input, password)
    

    @allure.step('Нажимаю на кнопку показать пароль')
    def click_show_password_button(self):
        self.click_element(RecoveryPasswordPageLocators.hide_password_button)

    @allure.step('Проверяю, что появился пароль')
    def check_password_visible(self, password):
        assert self.get_value_input(RecoveryPasswordPageLocators.password_input) == password

    @allure.step('Проверяю, что появился поле пароль')
    def wait_password_input_visible(self):
        self.wait_element_to_be_visible(RecoveryPasswordPageLocators.password_input)