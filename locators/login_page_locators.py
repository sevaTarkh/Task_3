from selenium.webdriver.common.by import By

class LoginPageLocators:
    recovery_password_button = [By.XPATH, "//a[text()='Восстановить пароль']"]
    email_input = [By.XPATH, "//label[text()='Email']/following-sibling::input[1]"]
    password_input = [By.XPATH, "//label[text()='Пароль']/following-sibling::input[1]"]
    sign_in_button = [By.XPATH, "//button[text()='Войти']"]
    sign_in_title = [By.XPATH, "//h2[text()='Вход']"]