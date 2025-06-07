import time

from playwright.sync_api import Page, expect, Playwright

from utils.api_base import APIUtils

# API call is made from server when link is clicked -> API call contacts server and returns fake request

fake_payload_order_response = {"data": [], "message": "No Orders"}

# order id = 6711e249ae2afd4c0b9f6fb0

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_network_request(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("smac7@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Pic_appl1")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Orders").click()
    page.get_by_role("button", name="view").first.click()
    #time.sleep(3)
    message = page.locator(".blink_me").text_content().strip()
    print(message)

def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    token_value = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # inject token to local storage
    page.add_init_script(f"""localStorage.setItem('token', '{token_value}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="Orders").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
