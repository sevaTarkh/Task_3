import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import allure
from data.data import Constants
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

from helpers.helpers import Helpers

class TestPersonalAccauntPage:
    @allure.title('Переход на страницу личного кабинета')
    @allure.description('Нажимаю на личный кабинет, проверяю ссылку')
    def test_check_redirect_to_personal_accaunt_page(self, browser, create_user_and_delete_after):

        login_pass_name = create_user_and_delete_after

        Helpers.login_user(browser, login_pass_name)

        profile_page = ProfilePage(browser)
        main_page = MainPage(browser)

        main_page.click_my_accaunt_button()
        profile_page.check_save_button_visibility()

    @allure.title('Переход в раздел история заказов')
    @allure.description('Нажимаю на личный кабинет, нажимаю на раздел "история заказов"')
    def test_check_redirect_to_history_orders(self, browser, create_user_and_delete_after):

        login_pass_name = create_user_and_delete_after

        Helpers.login_user(browser, login_pass_name)

        main_page = MainPage(browser)
        profile_page = ProfilePage(browser)

        main_page.click_my_accaunt_button()
        profile_page.click_history_orders_button()
        profile_page.check_current_url(Constants.url_burger_history_orders)

    @allure.title('Выход из аккаунта')
    @allure.description('Нажимаю на личный кабинет, нажимаю на выход')
    def test_check_after_logout_redirect_to_login(self, browser, create_user_and_delete_after):

        login_pass_name = create_user_and_delete_after

        Helpers.login_user(browser, login_pass_name)

        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        profile_page = ProfilePage(browser)

        main_page.click_my_accaunt_button()
        profile_page.click_logout_button()

        login_page.check_login_page()