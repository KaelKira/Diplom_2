from client.client import UserAPIClient
import allure
from helpers.helpers import Helpers


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и валидными ингредиентами")
    def test_create_order_with_auth(self):
        helper = Helpers()
        client = UserAPIClient()
        ingredients = helper.get_valid_ingredients()
        response_user = helper.create_user_get_token()
        token_auth = response_user['accessToken']
        payload ={
            "ingredients": ingredients[:2]
        }
        response = client.post_orders(data=payload, header={"Authorization": token_auth})
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        helper = Helpers()
        client = UserAPIClient()
        ingredients = helper.get_valid_ingredients()
        payload ={
            "ingredients": ingredients[:2]
        }
        response = client.post_orders(data=payload)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        helper = Helpers()
        client = UserAPIClient()
        response_user = helper.create_user_get_token()
        token_auth = response_user['accessToken']
        response = client.post_orders(data={"ingredients": []}, header={"Authorization": token_auth})
        assert response.status_code == 400
        assert response.json().get("message") == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным ингредиентом")
    def test_create_order_with_invalid_ingredient(self):
        helper = Helpers()
        client = UserAPIClient()
        response_user = helper.create_user_get_token()
        token_auth = response_user['accessToken']
        response = client.post_orders(data={"ingredients": "invalid_id"}, header={"Authorization": token_auth})
        assert response.status_code == 500