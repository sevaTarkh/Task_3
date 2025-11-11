import requests
from datetime import datetime
from data.data import Constants
import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from pages.main_page import MainPage
from pages.login_page import LoginPage

class Helpers:

    def create_user():

        unique_email = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}@mail.ru"
        unique_name = f"seva{datetime.now().strftime("%m%d%H%M%S%f")}"
        password = Constants.password

        payload = {
            "email": unique_email,
            "password": password,
            "name": unique_name,
        }
        response = requests.post(f"{Constants.url_burger}api/auth/register", data=payload)
        
        if response.status_code == 200:
            return [response.json()['user']['email'], password, response.json()['user']['name'], response.json()['accessToken']]
        

    def login_user(browser, login_pass):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        main_page.click_my_accaunt_button()
        login_page.fill_email_input(login_pass[0])
        login_page.fill_password_input(login_pass[1])

        login_page.click_sign_in_button()


    def create_order(browser):
        main_page = MainPage(browser)

        main_page.move_bun_to_burger(browser)
        main_page.click_create_order_button()
        time.sleep(1)
        main_page.click_close_order_button()

