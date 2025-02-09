import json
import requests
import random
import string
import data
from client.client import UserAPIClient


class Helpers:
# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def create_user_get_token(self):
        email = self.generate_random_string(10) + '@ya.ru'
        name = self.generate_random_string(10)
        password = self.generate_random_string(10)
        payload = {
            "email": email,
            'password': password,
            'name': name
        }
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        response = client.post_auth_register(data_register=payload_string)
        credentials = payload
        credentials['accessToken'] = response.json()['accessToken']
        credentials['refreshToken'] = response.json()['refreshToken']
        credentials['response'] = response
        return credentials

    def get_valid_ingredients(self):
        client = UserAPIClient()
        response = client.get_ingredients()
        return [ingredient["_id"] for ingredient in response.json().get("data", [])]


