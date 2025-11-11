import allure
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step('Нажимаю на кнопку Восстановить пароль')
    def click_recovery_password_button(self):
        self.click_element(LoginPageLocators.recovery_password_button)


    @allure.step('Ввожу пароль')
    def fill_password_input(self, password):
        self.send_keys_to_input(LoginPageLocators.password_input, password)


    @allure.step('Ввожу email')
    def fill_email_input(self, email):
        self.send_keys_to_input(LoginPageLocators.email_input, email)


    @allure.step('Нажимаю на кнопку "Войти"')
    def click_sign_in_button(self):
        self.click_element(LoginPageLocators.sign_in_button)

    @allure.step('Проверяю, что нахожусь на странцие логин')
    def check_login_page(self):
        self.wait_element_to_be_visible(LoginPageLocators.sign_in_title)