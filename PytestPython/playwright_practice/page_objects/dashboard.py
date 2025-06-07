from .orders_history import OrdersHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="Orders").click()
        orders_history_page = OrdersHistoryPage(self.page)
        return orders_history_page