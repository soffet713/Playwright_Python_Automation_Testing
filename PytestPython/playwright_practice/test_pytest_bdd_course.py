import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios

from page_objects.global_variables import *
from page_objects.login import LoginPage
from utils.api_base_framework import APIUtils


scenarios('features/order_transaction.feature')

@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(username, password, playwright:Playwright, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright, user_credentials)
    shared_data['order_id'] = orderId


@given('the user is on the landing page')
def user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate(login_url)
    shared_data['login_page'] = login_page


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(username, password)
    shared_data['dashboard_page'] = dashboard_page


@when('navigate to the Orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    order_history_page = dashboard_page.selectOrdersNavLink()
    shared_data['orderHistory_page'] = order_history_page


@when('Select the OrderId')
def select_order_id(shared_data):
    order_history_page = shared_data['orderHistory_page']
    order_id = shared_data['order_id']
    orders_details_page = order_history_page.selectOrder(order_id)
    shared_data['order_details_page'] = orders_details_page


@then('Order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orders_details_page = shared_data['order_details_page']
    orders_details_page.verifyOrderMessage()
