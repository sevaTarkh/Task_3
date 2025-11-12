import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import allure
from pages.main_page import MainPage
from pages.list_of_orders_page import ListOfOrdersPage

from helpers.helpers import Helpers
from pages.profile_page import ProfilePage

class TestListOfOrdersPage:
    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Проверяю счетчик за все время, оформляю заказ проверяю, что количество изменилось')
    def test_check_edit_orders_for_all_time(self, browser, create_user_and_delete_after):

        main_page = MainPage(browser)
        list_of_orders_page = ListOfOrdersPage(browser)
        main_page.click_list_of_orders_button()

        current_all_time_orders = list_of_orders_page.check_order_all_time()

        login_pass_name = create_user_and_delete_after
        Helpers.login_user(browser, login_pass_name)
        Helpers.create_order(browser)

        main_page.click_list_of_orders_button()

        expected_all_time_orders = list_of_orders_page.check_order_all_time()

        list_of_orders_page.check_count_orders(current_all_time_orders, expected_all_time_orders)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Проверяю счетчик за сегодня, оформляю заказ проверяю, что количество изменилось')
    def test_check_edit_orders_today(self, browser, create_user_and_delete_after):
        main_page = MainPage(browser)
        list_of_orders_page = ListOfOrdersPage(browser)

        main_page.click_list_of_orders_button()
        current_today_orders = list_of_orders_page.check_order_today()

        login_pass_name = create_user_and_delete_after
        Helpers.login_user(browser, login_pass_name)

        Helpers.create_order(browser)
        main_page.click_list_of_orders_button()

        expected_today_orders = list_of_orders_page.check_order_today()

        list_of_orders_page.check_count_orders(current_today_orders, expected_today_orders)
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Перехожу в заказы, нажимаю на заказ')
    def test_check_orders_details(self, browser): 
        list_of_orders_page = ListOfOrdersPage(browser)
        main_page = MainPage(browser)

        main_page.click_list_of_orders_button()

        list_of_orders_page.click_order()
        list_of_orders_page.check_order_details()

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('Проверяю счетчик за сегодня, оформляю заказ проверяю, что количество изменилось')
    def test_check_number_order_in_work(self, browser, create_user_and_delete_after):
        profile_page = ProfilePage(browser)
        main_page = MainPage(browser)
        list_of_orders_page = ListOfOrdersPage(browser)

        login_pass_name = create_user_and_delete_after
        Helpers.login_user(browser, login_pass_name)
        Helpers.create_order(browser)

        main_page.click_my_accaunt_button()
        profile_page.click_history_orders_button()

        number = profile_page.get_last_order_number()

        main_page.click_list_of_orders_button()

        list_of_orders_page.wait_order_in_work()

        list_of_orders_page.check_number_order_in_work(number[1::])


    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Проверяю счетчик за сегодня, оформляю заказ проверяю, что количество изменилось')
    def test_check_numbers_order_in_all_orders(self, browser, create_user_and_delete_after):
        profile_page = ProfilePage(browser)
        main_page = MainPage(browser)
        list_of_orders_page = ListOfOrdersPage(browser)


        login_pass_name = create_user_and_delete_after
        Helpers.login_user(browser, login_pass_name)
        Helpers.create_order(browser)

        main_page.click_my_accaunt_button()
        profile_page.click_history_orders_button()

        numbers = profile_page.get_all_orders_numbers()

        main_page.click_list_of_orders_button()

        list_of_orders_page.check_numbers_in_list(numbers)


