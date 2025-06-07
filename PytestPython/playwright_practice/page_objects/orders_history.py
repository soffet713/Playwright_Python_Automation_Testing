from playwright.sync_api import expect

from .order_details import OrderDetailsPage


class OrdersHistoryPage:
    def __init__(self, page):
        self.page = page

    def view_order(self, order_id):
        order_row = self.page.locator("tr").filter(has_text=order_id)
        order_row.get_by_role("button", name="View").click()
        order_details_page = OrderDetailsPage(self.page)
        return order_details_page