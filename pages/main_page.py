import allure
import sys
import os
from seletools.actions import drag_and_drop
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step('Нажимаю на кнопку Войти в аккаунт')
    def click_login_button(self):
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.login_in_accaunt_button)

    @allure.step('Нажимаю на кнопку личный кабинет')
    def click_my_accaunt_button(self):
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.my_accaunt_button)

    @allure.step('Нажимаю на кнопку констурктор')
    def click_constructor_button(self):
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.constructor_button)

    @allure.step('Нажимаю на кнопку лента заказов')
    def click_list_of_orders_button(self):
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.list_of_orders_button)

    @allure.step('Проверяю что отображается заголовок "Соберите бургер"')
    def check_visibility_title_create_burger(self):
        self.wait_element_to_be_visible(MainPageLocators.create_burger_title)

    @allure.step('Проверяю что отображается детали ингредиента')
    def check_visibility_information_ingredient(self):
        self.wait_element_to_be_visible(MainPageLocators.ingredients_details)

    @allure.step('Нажимаю на булку')
    def click_bun_button(self):
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.ingredient)

    @allure.step('Нажимаю на крестик закрытия деталей ингредиентов')
    def click_close_button(self):
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.close_details_button)

    @allure.step('Проверяю, что появился номер заказа')
    def check_number_of_order(self):
        self.wait_change_value(MainPageLocators.number_of_order, '9999')

    @allure.step('Нажимаю на крестик закрытия заказа')
    def click_close_order_button(self):
        self.check_number_of_order()
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.close_order_button)

    @allure.step('Проверяю, что закролось окно деталей')
    def check_details_wimdow_hidden(self):
        self.wait_element_to_be_hidden(MainPageLocators.ingredients_details_window)

    @allure.step('Добавляю булку в заказ')
    def move_bun_to_burger(self, driver):
        self.wait_element_to_be_visible(MainPageLocators.ingredient)
        source = self.find_element(MainPageLocators.ingredient)
        target = self.find_element(MainPageLocators.burger_constructor)
        drag_and_drop(driver, source, target)

    @allure.step('Проверяю, чему равно сумма')
    def check_sum_order(self, summa):
        assert self.get_text(MainPageLocators.summa_order) == summa

    @allure.step('Нажимаю на оформление заказа')
    def click_create_order_button(self):
        self.wait_element_to_be_cliackable_and_click(MainPageLocators.create_order)

    @allure.step('Проверяю что отображается сообщение создания заказа')
    def check_success_order_creation(self):
        self.wait_element_to_be_visible(MainPageLocators.success_text)



