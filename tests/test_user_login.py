import json
import allure
import pytest
from client.client import UserAPIClient
from helpers.helpers import Helpers


class TestUserLogin:

    @allure.title('Логин под существующим пользователем')
    def test_user_login_happy_pass(self):
        helper = Helpers()
        client = UserAPIClient()
        response = helper.create_user_get_token()
        payload = {
            "email": response['email'],
            "password": response['password']
        }
        payload_string = json.dumps(payload)
        response_login = client.post_auth_login(data_login=payload_string)
        assert response_login.status_code == 200 and 'accessToken' in response_login.text

    @allure.title('Логин с неверным логином или паролем')
    @pytest.mark.parametrize(
        'password, email',
        [
            ['say_pass_and_go_123123', 'ivan777@ya.ru'],
            ['say_pass_and_go', 'ivan777123123@ya.ru'],
            ['', '']
        ]
    )
    def test_user_login_wrong_data(self, password, email):
        client = UserAPIClient()
        payload = {
            "email": email,
            "password": password
        }
        payload_string = json.dumps(payload)
        response_login = client.post_auth_login(data_login=payload_string)
        assert response_login.status_code == 401 and 'email or password are incorrect' in response_login.text
