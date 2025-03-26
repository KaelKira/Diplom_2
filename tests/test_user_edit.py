import allure
import pytest

from client.client import UserAPIClient
from helpers.helpers import Helpers


class TestUserEdit:

    @allure.title('Изменение пользователя c авторизацией')
    @pytest.mark.parametrize(
        'input_to_edit',
        [
            ['name'],
            ['email']
        ]
    )
    def test_user_edit_info(self, input_to_edit):
        helper = Helpers()
        client = UserAPIClient()
        response_user = helper.create_user_get_token()
        token_auth = response_user['accessToken']
        value = helper.generate_random_string(10) + 'ya.ru'
        updated_data = {
            input_to_edit[0]: value
        }
        response = client.patch_auth_user(data=updated_data, header={"Authorization": token_auth})
        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json().get("user")[input_to_edit[0]] == value


    @allure.title('Изменение пользователя без авторизации')
    def test_user_edit_info_without_login(self):
        helper = Helpers()
        client = UserAPIClient()
        helper.create_user_get_token()
        updated_data = {"name": "NewName"}
        response = client.patch_auth_user(data=updated_data, header={"Authorization": ''})
        assert response.status_code == 401
        assert 'You should be authorised' in response.text

    @allure.title('Изменение пользователя - поле email, существующий email')
    def test_user_edit_info_without_login(self):
        helper = Helpers()
        client = UserAPIClient()
        response_user = helper.create_user_get_token()
        token_auth = response_user['accessToken']
        updated_data = {"email": "crnit123prfe@ya.ru"}
        response = client.patch_auth_user(data=updated_data, header={"Authorization": token_auth})
        assert response.status_code == 403
        assert '"User with such email already exists"' in response.text