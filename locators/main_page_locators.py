from selenium.webdriver.common.by import By

class MainPageLocators:
    login_in_accaunt_button = [By.XPATH, "//button[text()='Войти в аккаунт']"]
    my_accaunt_button = [By.XPATH, "//p[text()='Личный Кабинет']"]
    list_of_orders_button = [By.XPATH, "//p[text()='Лента Заказов']"]
    constructor_button = [By.XPATH, "//p[text()='Конструктор']"]
    create_burger_title = [By.XPATH, "//h1[text()='Соберите бургер']"]
    ingredients_details = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    ingredient = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"]
    close_details_button = [By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']//following-sibling::button[1]"]
    close_order_button = [By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']//following-sibling::button[1]"]
    ingredients_details_window = [By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']"]
    burger_constructor = [By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']"]
    summa_order = [By.XPATH, "//p[@class='text text_type_digits-medium mr-3']"]
    create_order = [By.XPATH, "//button[text()='Оформить заказ']"]
    success_text = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
    modal_window = [By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"]
    number_of_order = [By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"]