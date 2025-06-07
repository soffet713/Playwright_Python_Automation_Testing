import time

import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from page_objects.global_variables import *
from page_objects.login import LoginPage
from utils.api_base_framework import APIUtils

scenarios("features/order_transaction.feature")

@pytest.fixture
def shared_data():
    return {}

@given('The user is on the login page')
def user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate(login_url)
    shared_data['login_page'] = login_page

@given(parsers.parse('they login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    shared_data["user_credentials"] = user_credentials
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(shared_data['user_credentials'])
    time.sleep(5)
    shared_data['dashboard_page'] = dashboard_page

@when(parsers.parse('I place the item order with {username} and {password}'))
def place_item_order(shared_data, username, password, playwright):
    api_utils_framework = APIUtils()
    time.sleep(3)
    order_id = api_utils_framework.create_order(playwright, shared_data['user_credentials'])
    time.sleep(3)
    shared_data['order_id'] = order_id

@when('navigate to the Orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    order_history_page = dashboard_page.selectOrdersNavLink()
    time.sleep(5)
    shared_data['order_history_page'] = order_history_page

@when('Select the OrderId')
def select_order_id(shared_data):
    order_history_page = shared_data['order_history_page']
    order_id = shared_data['order_id']
    order_details_page = order_history_page.view_order(order_id)
    shared_data['order_details_page'] = order_details_page

@then('Order message is successfully displayed')
def order_message_displayed(shared_data):
    order_details_page = shared_data['order_details_page']
    order_details_page.verify_message(successful_order_msg)
