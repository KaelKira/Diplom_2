from client.client import UserAPIClient
import allure
from helpers.helpers import Helpers


class TestGetUserOrders:
    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_user_orders_authorized(self):
        helper = Helpers()
        client = UserAPIClient()
        response_user = helper.create_user_get_token()
        token_auth = response_user['accessToken']
        response = client.get_orders(header={"Authorization": token_auth})
        orders = response.json()["orders"]

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "orders" in response.json()
        assert len(orders) == 0

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_user_orders_unauthorized(self):
        client = UserAPIClient()
        response = client.get_orders(data='')

        assert response.status_code == 401
        assert response.json().get("success") is False
