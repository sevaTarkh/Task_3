import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.chrome.options import Options as ChromeOptions
from helpers.helpers import Helpers
import requests
from data.data import UrlConstants

@pytest.fixture(params=['chrome', 'firefox'])
def browser(request):
    driver = None
    if request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    elif request.param == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized") 
        chrome_options.add_argument("--width=1920")
        chrome_options.add_argument("--height=1080")
        chrome_options.add_argument("--disable-extensions")  
        driver = webdriver.Chrome(options=chrome_options)

    driver.get(UrlConstants.url_burger)
    yield driver
    driver.quit()

@pytest.fixture
def create_user_and_delete_after():

    login_pass_name = Helpers.create_user()
    yield login_pass_name

    if login_pass_name:  
        payload = {
            "email": login_pass_name[0],
            "password": login_pass_name[1],
            "name": login_pass_name[2]
        }
        
        response = requests.post(f"{UrlConstants.url_burger}api/auth/login", data=payload)
        if response.status_code == 200:
            user_token = response.json()["accessToken"]
            requests.delete(f"{UrlConstants.url_burger}api/auth/user", headers={'Authorization': user_token})




