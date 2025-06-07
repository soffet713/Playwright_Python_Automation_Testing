from .dashboard import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def login(self, user_credentials):
        self.page.get_by_placeholder("email@example.com").fill(user_credentials['userEmail'])
        self.page.get_by_placeholder("enter your passsword").fill(user_credentials['userPassword'])
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = DashboardPage(self.page)
        return dashboard_page
