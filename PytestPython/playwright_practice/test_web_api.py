import time

from playwright.sync_api import Playwright, expect

from utils.api_base import APIUtils


# login: smac7@gmail.com password: Pic_appl1

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order and Grab Order ID
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("smac7@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Pic_appl1")
    page.get_by_role("button", name="Login").click()
    # time.sleep(4)

    # Submit order using API and verify order is present
    page.get_by_role("button", name="Orders").click()
    order_row = page.locator("tr").filter(has_text=order_id)
    order_row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
