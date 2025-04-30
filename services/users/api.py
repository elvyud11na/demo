import requests
import allure


from services.users.models.model_update_user import UpdateUserInfoModel
from services.users.models.model_users_by_credentials import UserCredentialsModel
from utils.helper import Helper
from config.headers import Headers
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints

from services.users.models.model_list_of_users import UserListModel
from services.users.models.model_user import UserModel


class UsersAPI(Helper):

    def __init__(self):
        self._payloads = Payloads()
        self._endpoints = Endpoints()
        self._headers = Headers()

    @allure.step("Get all users")
    def get_all_users(self, offset=0, limit=10, expected_result=True) -> UserListModel:
        response = requests.get(
            url=self._endpoints.get_users,
            headers=self._headers.basic,
            params={
                "offset": offset,
                "limit": limit
            },
            verify=False
        )
        self.attach_response(response.json())  # прикрепляем в отчет ответ
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UserListModel(**response.json())
            return model                             #для того чтобы могли передать какой либо парамент в другой эндпоинт, например в первом запросе создали юзера, а во втором проверям по его uuid что он есть в списке пользователей
        else:
            assert response.status_code !=200, response.json()



    @allure.step("Create user")
    def create_user(self, expected_result=True) -> UserModel:
        response = requests.post(
            url=self._endpoints.create_user,
            headers=self._headers.basic,
            json=self._payloads.create_user_payload(),
            verify=False
        )
        self.attach_response(response.json())
        if expected_result==True:
            assert response.status_code == 200, response.json()
            model = UserModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()


    @allure.step("Get user by uuid")
    def get_user_by_uuid(self, uuid, expected_result=True) -> UserModel:
        response = requests.get(
            url=self._endpoints.get_user_by_uuid(uuid),
            headers=self._headers.basic,
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UserModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()




    @allure.step("получить пользователя, используя учетные данные")
    def get_user_using_credentials(self, email, password, expected_result=True) -> UserCredentialsModel:
        response = requests.post(
            url=self._endpoints.get_user_using_credentials,
            headers=self._headers.basic,
            json=self._payloads.get_user_using_credentials(email=email, password=password),
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UserCredentialsModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()


    @allure.step("Update a user.")
    def update_user(self, uuid, email, name, nickname, expected_result=True) -> UpdateUserInfoModel:
        response = requests.patch(
            url=self._endpoints.update_user(uuid),
            headers=self._headers.basic,
            json=self._payloads.update_user(email=email, name=name, nickname=nickname),
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UpdateUserInfoModel(**response.json())
            return model
        else:
            assert response.status_code == 409, response.json()
            print(response.json())
            error_message = 'already exists'
            assert error_message in response.text
            #raise Exception('User already exists')


    @allure.step("Delete user by uuid")
    def delete_user_by_uuid(self, uuid, expected_result=True):
        response = requests.delete(
            url=self._endpoints.delete_user(uuid),
            headers=self._headers.basic,
            verify=False
        )
        if expected_result:
            assert response.status_code == 204, response.json()
            return response
        else:
            assert response.status_code == 404, response.json()
        self.attach_response(response.json())

    #from typing import List

    # def check_start_position(users: List[dict], offset: int):
    #     """Проверяет, что список пользователей начинается с позиции offset."""
    #     start_index = offset * len(users)
    #     first_user = users[start_index]
    #     if first_user:
    #         return True
    #     return False
