import allure
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):


    @allure.step('Нажимаю на кнопку история заказов')
    def click_history_orders_button(self):
        self.wait_element_to_be_cliackable_and_click(ProfilePageLocators.history_orders_button)

    @allure.step('Нажимаю на кнопку выход')
    def click_logout_button(self):
        self.wait_element_to_be_cliackable_and_click(ProfilePageLocators.logout_button)

    @allure.step('Проверяю видимость кнопки сохранить')
    def check_save_button_visibility(self):
        self.wait_element_to_be_visible(ProfilePageLocators.save_button)

    @allure.step('Получаю номер последнего заказа')
    def get_last_order_number(self):
        self.wait_element_to_be_visible(ProfilePageLocators.number_of_last_order)
        return self.get_text(ProfilePageLocators.number_of_last_order)

    @allure.step('Получаю все номера заказов')
    def get_all_orders_numbers(self):
        numbers = self.find_elements(ProfilePageLocators.numbers_of_all_orders)
        numbers_list = [number.text for number in numbers]
        return numbers_list