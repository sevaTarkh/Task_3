import allure
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.list_of_orders_locatots import ListOfOrdersPageLocators
from pages.base_page import BasePage

class ListOfOrdersPage(BasePage):

    @allure.step('Проверяю, что нахожусь на странцие заказов')
    def check_list_of_orders_title(self):
        self.wait_element_to_be_visible(ListOfOrdersPageLocators.list_of_orders_title)


    @allure.step('Нажимаю на первый заказ')
    def click_order(self):
        self.wait_element_to_be_cliackable_and_click(ListOfOrdersPageLocators.first_order)

    @allure.step('Проверяю, что появились детали заказа')
    def check_order_details(self):
        self.wait_element_to_be_visible(ListOfOrdersPageLocators.burger_composition)

    @allure.step('Проверяю, количество заказов сегодня')
    def check_order_today(self):
        self.wait_element_to_be_visible(ListOfOrdersPageLocators.orders_today)
        return self.get_text(ListOfOrdersPageLocators.orders_today)

    @allure.step('Проверяю, количество заказов за все время')
    def check_order_all_time(self):
        self.wait_element_to_be_visible(ListOfOrdersPageLocators.orders_for_all_time)
        return self.get_text(ListOfOrdersPageLocators.orders_for_all_time)

    @allure.step('Проверяю, что количество заказов изменилось')
    def check_count_orders(self, orders, expected_orders):
        assert int(orders) < int(expected_orders)

    @allure.step('Проверяю, что количество заказов изменилось')
    def check_count_orders(self, orders, expected_orders):
        assert int(orders) < int(expected_orders)

    @allure.step('Проверяю, что заказ в списке заказов')
    def check_number_order_in_work(self, number):
        orders = self.find_elements(ListOfOrdersPageLocators.orders_in_work)
        order_numbers = [order.text for order in orders]

        assert number in order_numbers

    @allure.step('Жду появление заказа в работе')
    def wait_order_in_work(self):
        self.wait_element_to_be_visible(ListOfOrdersPageLocators.orders_in_work)


    @allure.step('Есть ли номер заказа')
    def check_numbers_in_list(self, numbers_list):
        numbers = self.find_elements(ListOfOrdersPageLocators.number_of_all_orders)
        numbers_of_all_orders = [number.text for number in numbers]

        for i in range(len(numbers_list)):
            assert numbers_list[i] in numbers_of_all_orders 

    