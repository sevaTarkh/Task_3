from selenium.webdriver.common.by import By

class RecoveryPasswordPageLocators:
    email_input = [By.XPATH, "//input[@name='name']"]
    recovery_button = [By.XPATH, "//button[text()='Восстановить']"]
    code_input = [By.XPATH, "//label[text()='Введите код из письма']"]
    password_input = [By.XPATH, "//input[@name='Введите новый пароль']"]
    hide_password_button = [By.XPATH, "//div[@class='input__icon input__icon-action']/*"]