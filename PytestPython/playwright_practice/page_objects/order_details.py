from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self, page):
        self.page = page

    def verify_message(self, message):
        expect(self.page.locator(".tagline")).to_contain_text(message)