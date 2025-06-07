from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page:Page):
    # Dynamically choose the iPhone X and Nokia Edge, and add them both to cart, then verify
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")  # input component should be wrapped within label
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    checkout_button = page.get_by_text("Checkout")
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    expect(checkout_button).to_contain_text("Checkout ( 1 )")
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    expect(checkout_button).to_contain_text("Checkout ( 2 )")
    checkout_button.click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.locator(".media-body").locator(".media-heading").get_by_text("iphone X")).to_be_visible()
    expect(page.locator(".media-body").locator(".media-heading").get_by_text("Nokia Edge")).to_be_visible()

def test_child_window_handling(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").get_by_text("Free Access to Interview").click()
        child_page = new_page_info.value
        notice_text = child_page.locator(".red")
        text = child_page.locator(".red").text_content()
        # print(text)
        words = text.split("at")
        # print(words[1])
        email = words[1].split("with")
        email_text = email[0].strip()
        # print(email[0].strip())
        assert email_text == "mentor@rahulshettyacademy.com"
