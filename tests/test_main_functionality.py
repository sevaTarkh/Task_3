import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import allure
from data.data import Constants
from pages.main_page import MainPage
from pages.list_of_orders_page import ListOfOrdersPage

from helpers.helpers import Helpers

class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Нахожусь не в конструкторе, нажимаю на конструктор, проверяю ссылку')
    def test_check_redirect_to_constructor_page(self, browser):


        main_page = MainPage(browser)

        main_page.click_list_of_orders_button()
        main_page.click_constructor_button()
        main_page.check_visibility_title_create_burger()

    @allure.title('Переход по клику на Лента заказов')
    @allure.description('Нажимаю на лента заказов, проверяю ссылку')
    def test_check_redirect_to_list_orders_page(self, browser):
        main_page = MainPage(browser)
        list_orders_page = ListOfOrdersPage(browser)

        main_page.click_list_of_orders_button()
        list_orders_page.check_list_of_orders_title()


    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Нажимаю на ингредиент, проверяю что появились детали')
    def test_after_click_check_ingredient_information(self, browser):


        main_page = MainPage(browser)

        main_page.click_bun_button()

        main_page.check_visibility_information_ingredient()


    @allure.title('Всплывающее окно с деталями закрывается на крестик')
    @allure.description('Нажимаю на ингредиент, проверяю что появились детали, закрываю')
    def test_close_ingredient_information(self, browser):


        main_page = MainPage(browser)

        main_page.click_bun_button()

        main_page.click_close_button()
        main_page.check_details_wimdow_hidden()


    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Добавляю ингредиент, проверяю что появились счетчик увеличился')
    def test_add_ingredient_check_counter(self, browser):

        
        main_page = MainPage(browser)

        main_page.move_bun_to_burger(browser)
        main_page.check_sum_order(Constants.summa)


    @allure.title('Создание заказа')
    @allure.description('Добавляю ингредиент, оформляю заказ')
    def test_create_order(self, browser, create_user_and_delete_after):


        login_pass_name = create_user_and_delete_after
        Helpers.login_user(browser, login_pass_name)

        main_page = MainPage(browser)

        main_page.move_bun_to_burger(browser)
        main_page.click_create_order_button()
        main_page.check_success_order_creation()


