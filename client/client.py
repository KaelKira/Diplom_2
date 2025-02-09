import requests
import data


class UserAPIClient:
    host = data.HOST
    headers = {"Content-type": "application/json"}

    def post_auth_register(self, data_register=None):
        url = f"{self.host}/api/auth/register"
        return requests.post(url=url, data=data_register, headers=self.headers)

    def post_auth_login(self, data_login=None):
        url = f"{self.host}/api/auth/login"
        return requests.post(url=url, data=data_login, headers=self.headers)

    def post_auth_user(self, data_login=None):
        url = f"{self.host}/api/auth/user"
        return requests.post(url=url, data=data_login, headers=self.headers)

    def get_auth_user(self, data_login=None, header=None):
        url = f"{self.host}/api/auth/user"
        return requests.get(url=url, data=data_login, headers=header)

    def patch_auth_user(self, data=None, header=None):
        url = f"{self.host}/api/auth/user"
        return requests.patch(url=url, data=data, headers=header)

    def get_auth_login(self, data_login=None):
        url = f"{self.host}/api/auth/login"
        return requests.get(url=url, data=data_login, headers=self.headers)

    def post_auth_logout(self, data_logout=None):
        url = f"{self.host}/api/auth/logout"
        return requests.get(url=url, data=data_logout, headers=self.headers)

    def get_ingredients(self):
        url = f"{self.host}/api/ingredients"
        return requests.get(url=url)

    def post_orders(self, data=None, header=None):
        url = f"{self.host}/api/orders"
        return requests.post(url=url, data=data, headers=header)

    def get_orders(self, data=None, header=None):
        url = f"{self.host}/api/orders"
        return requests.get(url=url, data=data, headers=header)