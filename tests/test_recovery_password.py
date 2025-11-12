import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import allure
from data.data import Constants, UrlConstants
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recovery_password_page import RecoveryPasswordPage

class TestRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('На странице ищем кнопку "Войти в аккаунт", нажимаем на нее, нажимаем на ссылку "Восстановить пароль", проверяем редирект')
    def test_check_redirect_to_recovery_page(self, browser):

        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        recovery_password_page = RecoveryPasswordPage(browser)
        main_page.click_login_button()
        login_page.click_recovery_password_button()

        recovery_password_page.check_current_url(UrlConstants.url_burger_recovery)

    @allure.title('Восстановления почты')
    @allure.description('Переходим на страницу "Восстановления пароля", вводим потчу, нажимаем кнопку восстановить, ждем появления воостановления пароля')
    def test_check_recovery_email(self, browser):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        recovery_password_page = RecoveryPasswordPage(browser)
        main_page.click_login_button()
        login_page.click_recovery_password_button()

        recovery_password_page.fill_email_input(Constants.new_email)
        recovery_password_page.click_recovery_button()
        recovery_password_page.check_code_visible()

    @allure.title('Проверка работы кнопки скрыть пароль')
    @allure.description('Переходим на страницу "Восстановления пароля", вводим потчу, нажимаем кнопку восстановить, вводим пароль нажимаем на кнопку скрыть пароль')
    def test_password_visible(self, browser):


        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        recovery_password_page = RecoveryPasswordPage(browser)

        main_page.click_login_button()
        login_page.click_recovery_password_button()

        recovery_password_page.fill_email_input(Constants.new_email)
        recovery_password_page.click_recovery_button()

        recovery_password_page.wait_password_input_visible()
        recovery_password_page.fill_password_input(Constants.new_password)

        recovery_password_page.click_show_password_button()

        recovery_password_page.check_password_visible(Constants.new_password)