import allure

from config.base_test import BaseTest
from services.users.payloads import Payloads

@allure.epic("Users")
class TestUsers(BaseTest):

    @allure.title("Получение списка пользователей")
    def test_get_all_users(self):
        all_users = self.api_users.get_all_users()
        print(f"UUID первого юзера: {all_users.users[0].uuid}")
   #!!!!! "API-3"

    @allure.title("Создание пользователя - 'API-3'")
    def test_create_users(self):
        user = self.api_users.create_user() # создали пользователя
        users_list = self.api_users.get_all_users(offset=0, limit=20)# получили список пользователей
        user_exists = any(element.email == user.email for element in users_list.users) # any проверяет удовлетворяет хотя бы один элемент из списка условию, у нас проверяетчто поле user.email есть в списке всех пользователей
       # проверяем что у хотя бы у одногоe lement из списка users_list.users есть емайл - element.email, который равен user.email-из стоки 15
        assert user_exists == True
        response = self.api_users.get_user_by_uuid(user.uuid)
        assert response.email == user.email
        assert response.name == user.name
        assert response.nickname == user.nickname

    @allure.title("Проверка невозможности обновления юзера уже занятыми данными- 'API-4'")
    def test_update_user_with_data_already_occupied(self):
        all_users = self.api_users.get_all_users()
        user_1_email = all_users.users[0].email
        user_1_nickname = all_users.users[0].nickname
        user_2_uuid = all_users.users[-1].uuid
        user_2_name = all_users.users[-1].name
        self.api_users.update_user(uuid=user_2_uuid, email=user_1_email, name=user_2_name, nickname=user_1_nickname, expected_result=False)




    @allure.title("Получение пользователя по uuid")
    def test_get_user_by_uuid(self):
        user = self.api_users.create_user()
        response = self.api_users.get_user_by_uuid(user.uuid)
        assert response.uuid == user.uuid



    @allure.title("Обновить данные пользователя по uuid")
    def test_update_user(self):
        user = self.api_users.create_user()
        user_email = user.email
        user_name = user.name
        user_nickname = user.nickname
        self.api_users.update_user(uuid=user.uuid, email="testcat5@mail.com", name="Alina", nickname="aaa")
        update_user = self.api_users.get_user_by_uuid(uuid=user.uuid)
        assert user.uuid == update_user.uuid, "uuid созданного юзера != обновляемому юзеру"
        assert user_email != update_user.email, user.json  # "email не обновился"
        assert user_name != update_user.name, "name не обновился"
        assert user_nickname != update_user.nickname, "nickname не обновился"

    @allure.title("Удаление  пользователя по uuid")
    def test_delete_user_by_uuid(self):
        user = self.api_users.create_user()
        self.api_users.delete_user_by_uuid(user.uuid)
        self.api_users.get_user_by_uuid(user.uuid, expected_result=False) # мы же знаем что такого юзера больше нет и поэтому expected_result = false
        users_list = self.api_users.get_all_users(offset=0, limit=20)  # получили список пользователей
        user_not_exists = any(element.uuid != user.uuid for element in users_list.users)
        user_not_exists == True


    # def test_create_and_delete_user(self, create_user):
    #     print(create_user)
    #     assert create_user is not None

