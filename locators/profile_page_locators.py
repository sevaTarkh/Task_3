from selenium.webdriver.common.by import By

class ProfilePageLocators:
    history_orders_button = [By.XPATH, "//a[text()='История заказов']"]
    logout_button = [By.XPATH, "//button[text()='Выход']"]
    save_button = [By.XPATH, "//button[text()='Сохранить']"]
    number_of_last_order = [By.XPATH, "(//p[@class='text text_type_digits-default'])[last()]"]
    numbers_of_all_orders = [By.XPATH, "//p[@class='text text_type_digits-default']"]