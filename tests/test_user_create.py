import json
import allure
import pytest
from client.client import UserAPIClient
from helpers.helpers import Helpers


class TestCreateUser:

    @allure.title('Успешное создание пользователя')
    def test_user_create_happy_pass(self):
        helper = Helpers()
        email = helper.generate_random_string(10) + '@ya.ru'
        name = helper.generate_random_string(10)
        password = helper.generate_random_string(10)
        payload = {
            "email": email,
            'password': password,
            'name': name
        }
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        response = client.post_auth_register(data_register=payload_string)
        assert response.status_code == 200 and email in response.text

    @allure.title('Cоздание пользователя, который уже зарегистрирован')
    def test_user_create_double_registration(self):
        helper = Helpers()
        email = helper.generate_random_string(10) + '@ya.ru'
        name = helper.generate_random_string(10)
        password = helper.generate_random_string(10)
        payload = {
            "email": email,
            'password': password,
            'name': name
        }
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        client.post_auth_register(data_register=payload_string)
        response = client.post_auth_register(data_register=payload_string)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('Создание пользователя без одного из обязательных полей')
    @pytest.mark.parametrize(
        'name, password, email',
        [
            ['', 'say_pass_and_go', 'ivan777@ya.ru'],
            ['Ivan', '', 'ivan777@ya.ru'],
            ['Ivan', 'say_pass_and_go', '']
        ]
    )
    def test_user_create_no_fields(self, name, password, email):
        text_error = 'Email, password and name are required fields'
        code = 403
        payload = {
            "email": email,
            'password': password,
            'name': name
        }
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        response = client.post_auth_register(data_register=payload_string)
        assert response.status_code == code and text_error in response.text