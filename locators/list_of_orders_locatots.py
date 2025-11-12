from selenium.webdriver.common.by import By

class ListOfOrdersPageLocators:
    list_of_orders_title = [By.XPATH, "//h1[text()='Лента заказов']"]
    first_order = [By.XPATH, "(//li[@class='OrderHistory_listItem__2x95r mb-6'])[1]"]
    burger_composition = [By.XPATH, "//p[text()='Cостав']"]
    orders_for_all_time = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]"]
    orders_today = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]"]
    orders_in_work = [By.XPATH, "//li[@class='text text_type_digits-default mb-2']"]
    all_orders_done = [By.XPATH, "//li[text()='Все текущие заказы готовы!']"]
    number_of_all_orders = [By.XPATH, "//p[@class='text text_type_digits-default']"]