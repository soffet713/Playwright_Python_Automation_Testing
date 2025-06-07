from playwright.sync_api import Playwright

order_payload = {"orders":[{"country":"India","productOrderedId":"67a8df56c0d3e6622a297ccd"}]}

class APIUtils:

    def get_token(self, playwright:Playwright):
        request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                         ignore_https_errors=True)
        token_response = request_context.post("/api/ecom/auth/login",
                                 data={"userEmail":"smac7@gmail.com","userPassword":"Pic_appl1"})
        assert token_response.ok
        print(token_response.json())
        response_body = token_response.json()
        return response_body["token"]


    def create_order(self, playwright:Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                         ignore_https_errors=True)
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=order_payload,
                                 headers={"Authorization": token, "Content-Type":"application/json"})
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id
