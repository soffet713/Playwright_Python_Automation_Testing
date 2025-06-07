import time

from playwright.sync_api import Page, expect, Playwright


def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # similar to opening browser incognito
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")
    # page.goto("https://www.killertechwolf.com/SeanProjects/Index.html")

# chromium headless mode, 1 single context
def test_playwright_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")

# --css selectors: id = #terms class = .text-info
def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy") # input component should be wrapped within label
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)

def test_wrong_credentials(page:Page):
    invalid_login_test(page)

def test_firefox_browser(playwright:Playwright):
    firefox_browser = playwright.firefox.launch(headless=False)
    context = firefox_browser.new_context()
    ff_page = context.new_page()
    invalid_login_test(ff_page)

def invalid_login_test(user_page):
    user_page.goto("https://rahulshettyacademy.com/loginpagePractise")
    user_page.get_by_label("Username:").fill("rahulshettyacademy")  # input component should be wrapped within label
    user_page.get_by_label("Password:").fill("learnbad")
    user_page.get_by_role("combobox").select_option("teach")
    user_page.locator("#terms").check()
    user_page.get_by_role("button", name="Sign In").click()
    expect(user_page.get_by_text("Incorrect username/password.")).to_be_visible()
