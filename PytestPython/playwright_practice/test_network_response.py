from playwright.sync_api import Page, expect

# API call is made from server when link is clicked -> API call contacts server and returns response

fake_payload_order_response = {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fake_payload_order_response
    )

def test_network_response(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("smac7@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Pic_appl1")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Orders").click()
    order_text = page.locator(".mt-4").text_content().strip()
    print(order_text)
    expect(page.locator(".mt-4")).to_contain_text("You have No Orders to show at this time. Please Visit Back Us")
