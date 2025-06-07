import pytest
from playwright.sync_api import Playwright


# Scope can also be set to class if tests are executed within a class and you only want the fixture executed once
@pytest.fixture(scope="session")
def pre_setup():
    print("Session setup the browser instance..")

@pytest.fixture(scope="session")
def browser_instance(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
