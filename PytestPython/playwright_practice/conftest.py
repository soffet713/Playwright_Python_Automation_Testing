import pytest
from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", choices=["chrome", "firefox"], help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="server selection"
    )

# request is a built-in global variable that can be used to access global environment variables

@pytest.fixture(scope="module")
def user_credentials(request):
    return request.param

@pytest.fixture
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.goto(url_name)
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch() # or other browser
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture()
def api_req(playwright: Playwright):
    request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                     ignore_https_errors=True)
    yield request_context
