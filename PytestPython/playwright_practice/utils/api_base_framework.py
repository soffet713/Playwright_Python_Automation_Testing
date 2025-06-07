import time

from playwright.sync_api import *

order_payload = {"orders":[{"country":"India","productOrderedId":"67a8df56c0d3e6622a297ccd"}]}

class APIUtils:

    def get_token(self, playwright:Playwright, user_credentials):
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                         ignore_https_errors=True)
        time.sleep(3)
        token_response = request_context.post("/api/ecom/auth/login",
                                 data={"userEmail":user_email,"userPassword":user_password})
        time.sleep(2)
        assert token_response.ok
        print(token_response.json())
        response_body = token_response.json()
        time.sleep(2)
        return response_body["token"]

    def get_token_bdd(self, playwright: Playwright, user_credentials):
        user_email = user_credentials["userEmail"]
        user_password = user_credentials["userPassword"]
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                         ignore_https_errors=True)
        token_response = request_context.post("/api/ecom/auth/login",
                                 data={"userEmail":user_email,"userPassword":user_password})
        assert token_response.ok
        print(token_response.json())
        response_body = token_response.json()
        return response_body["token"]


    def create_order(self, playwright:Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)
        time.sleep(3)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                         ignore_https_errors=True)
        time.sleep(2)
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=order_payload,
                                 headers={"Authorization": token, "Content-Type":"application/json"})
        time.sleep(2)
        print(response.json())
        time.sleep(2)
        response_body = response.json()
        time.sleep(3)
        order_id = response_body["orders"][0]
        return order_id

    def create_order_bdd(self, request, user_credentials):
        my_fixture = request.getfixturevalue("playwright")
        token = self.get_token_bdd(my_fixture, user_credentials)
        api_request_context = my_fixture.request.new_context(base_url="https://rahulshettyacademy.com",
                                                             ignore_https_errors=True)
        # api_request_context = request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)

        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=order_payload,
                                 headers={"Authorization": token, "Content-Type":"application/json"})
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id
