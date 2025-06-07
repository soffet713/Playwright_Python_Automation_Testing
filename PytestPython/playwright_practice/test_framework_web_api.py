import json
import pytest
from playwright.sync_api import Playwright, expect

from page_objects.global_variables import *
from page_objects.login import LoginPage
from utils.api_base_framework import APIUtils

# Plan: Create JSON file -> import data from JSON to util -> access information within test
with open('data/credentials.json') as json_file:
    test_data = json.load(json_file)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

# login: smac7@gmail.com password: Pic_appl1
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browser_instance, user_credentials):

    # Create Order and Grab Order ID
    api_utils_framework = APIUtils()
    order_id = api_utils_framework.create_order(playwright, user_credentials)

    # Create Login Page and Login
    login_page = LoginPage(browser_instance)
    login_page.navigate(login_url)
    dashboard_page = login_page.login(user_credentials)
    # time.sleep(4)

    # Submit order using API and verify order is present
    # Orders History Page, Order Detail Page, and verify pages
    orders_history_page = dashboard_page.selectOrdersNavLink()
    order_details_page = orders_history_page.view_order(order_id)
    order_details_page.verify_message(successful_order_msg)
