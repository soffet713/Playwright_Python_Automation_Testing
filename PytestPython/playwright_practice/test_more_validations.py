import time

from playwright.sync_api import Page, expect

# url = https://www.rahulshettyacademy.com/AutomationPractice/
def test_ui_checks(page:Page):
    # Hide/Display and Placeholder
    page.goto("http://www.rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    # time.sleep(3)

    # Alert Boxes
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    # time.sleep(4)

    # Mouse Hover
    page.locator("#mousehover").hover()
    # time.sleep(2)
    page.get_by_role("link", name="Top").click()
    # time.sleep(2)

    # Frame handling
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access Plan").click()
    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")

    # Table Checking / Handling
    # Check the price of rice and validate
    # Identify the price column first, then identify the rice row
    # Then, extract the price of the rice
    page.goto("http://www.rahulshettyacademy.com/seleniumPractise/#/offers")

    col_value = 0
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0 :
            col_value = index
            print(f"Price column index = {col_value}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    rice_price = rice_row.locator("td").nth(col_value).text_content()
    print(f"Price of rice is: {rice_price}")
    expect(rice_row.locator("td").nth(col_value)).to_have_text("37")
