
import allure
import pytest

from config.base_test import BaseTest



@allure.epic("Games")
class TestApi(BaseTest):

    @allure.title("Удаление  пользователя по uuid - 'API-1'")
    def test_delete_user_by_uuid(self):
        user = self.api_users.create_user()
        self.api_users.delete_user_by_uuid(user.uuid)
        self.api_users.get_user_by_uuid(user.uuid, expected_result=False)  # мы же занем что такого юзера больше нет и поэтому expected_result = false
        users_list = self.api_users.get_all_users(offset=0, limit=20)  # получили список пользователей
        user_not_exists = any(element.uuid != user.uuid for element in users_list.users)
        user_not_exists == True

    @allure.title(" Поиск игр по ключевым словам или фразе - API-2")
    @pytest.mark.parametrize(
        "search_word, expected_result", [
            (None, True),
            ("76437$FF", False)
        ])
    def test_search_game_by_word(self, search_word, expected_result):
        if expected_result:  # если тест позитивеый, то search_word будет равно из строки 34, если негативный то из берется из передаваемых значений
            game_list = self.api_games.get_games_list()
            first_game_title = game_list.games[0].title  # название игры Atomic Heart
            print(first_game_title)
            search_word = first_game_title.split(" ")[0].lower()  # часть названия игры получтлось atomic
            # print(search_word)
        search_game_by_word = self.api_games.search_game(0, 10, search_word, expected_result)
        # print(search_game_by_word)
        if expected_result:
            assert search_word in search_game_by_word.games[0].title.lower()
        else:
            assert search_game_by_word == None

    @allure.title("Создание пользователя - 'API-3'")
    def test_create_users(self):
        user = self.api_users.create_user()  # создали пользователя
        users_list = self.api_users.get_all_users(offset=0, limit=20)  # получили список пользователей
        user_exists = any(element.email == user.email for element in
                          users_list.users)  # any проверяет удовлетворяет хотя бы один элемент из списка условию, у нас проверяетчто поле user.email есть в списке всех пользователей
        # проверяем что у хотя бы у одногоe lement из списка users_list.users есть емайл - element.email, который равен user.email-из стоки 15
        assert user_exists == True
        response = self.api_users.get_user_by_uuid(user.uuid)
        assert response.email == user.email
        assert response.name == user.name
        assert response.nickname == user.nickname

    @allure.title("Проверка невозможности обновления юзера уже занятыми данными- 'API-4'")
    def test_update_user_with_data_already_occupied(self):
        all_users = self.api_users.get_all_users()
        #можно так аписать первого юзера и дальше через точку обращаться к его методам email,nickname
        # user_1 = all_users.users[0]
        # user_1.email
        user_1_email = all_users.users[0].email
        user_1_nickname = all_users.users[0].nickname
        user_2_uuid = all_users.users[-1].uuid
        self.api_users.update_user(uuid=user_2_uuid, email=user_1_email, name="gg", nickname=user_1_nickname,
                                   expected_result=False)

    @allure.step("Добавление игры в список желаемого юзера 'API-5'")
    def test_api_1(self):
        all_users = self.api_users.get_all_users()
        user_uuid = all_users.users[2].uuid
        wishlist_user_before = self.api_wishlist.get_users_wishlist_by_uuid(user_uuid)
        print(wishlist_user_before)
        game_list = self.api_games.get_games_list()
        game_uuid = [game.uuid for game in game_list.games]
        game_uuid_last = game_uuid[9]
        self.api_wishlist.add_item_wishlist(user_uuid, game_uuid_last)
        wishlist_user_after = self.api_wishlist.get_users_wishlist_by_uuid(user_uuid)
        assert str(wishlist_user_after.items[-1].uuid) == game_uuid_last
        assert wishlist_user_before != wishlist_user_after



    @allure.title("Получения списка пользователей с использованием пагинации - API-6")
    def test_get_user_with_pagination(self):
        all_users = self.api_users.get_all_users(offset=0, limit=2)
        user_1_uuid = all_users.users[0].uuid
        user_2_uuid = all_users.users[1].uuid
        assert len(all_users.users) == 2
        assert str(all_users.users[0].uuid) == str(user_1_uuid)
        all_users = self.api_users.get_all_users(offset=1, limit=3)
        assert len(all_users.users) == 3
        assert str(all_users.users[0].uuid) == str(user_2_uuid)
        # if self.api_users.check_start_position(all_users.users, 0):
        #     print("Список пользователей начинается с нулевой позиции.")
        # else:
        #     print("Список пользователей не начинается с нулевой позиции.")

    @allure.title("получить пользователя, используя учетные данные 'API-7'")
    def test_get_user_using_credentials(self):
        user = self.api_users.create_user()
        user_uuid = user.uuid
        get_user = self.api_users.get_user_using_credentials(user.email, "wqwewewr1!!")
        get_user_uuid = get_user.uuid
        assert user_uuid == get_user_uuid

    @allure.title("Удаление товара из списка желаний - API-8")
    def test_removing_product_from_wishlist(self):
        all_users = self.api_users.get_all_users(offset=0, limit=10)
        user_1_uuid = all_users.users[0].uuid
        games_list = self.api_games.get_games_list()
        new_game_uuid = games_list.games[0].uuid    #первая игра из списка игр
        self.api_wishlist.add_item_wishlist(user_1_uuid, new_game_uuid)
        wishlist_user_after_add_game = self.api_wishlist.get_users_wishlist_by_uuid(user_1_uuid)
        last_game_uuid_in_wishlist_user = wishlist_user_after_add_game.items[-1].uuid #игра добавляется в конец списка поэтому перем последний uuid
        assert str(last_game_uuid_in_wishlist_user) == new_game_uuid
        self.api_wishlist.remove_item_wishlist(user_1_uuid, str(last_game_uuid_in_wishlist_user))
        wishlist_user_after_remove_game = self.api_wishlist.get_users_wishlist_by_uuid(user_1_uuid)
        all_uuid_games = [items.uuid for items in wishlist_user_after_remove_game.items]
        assert last_game_uuid_in_wishlist_user not in all_uuid_games

    @allure.title("Получение информации об игре по ее ID - API-9")
    def test_game_by_uuid(self):
        game_list = self.api_games.get_games_list()
        game_uuid = game_list.games[2].uuid
        game_title = game_list.games[2].title
        game_price = game_list.games[2].price
        game_category_uuids = game_list.games[2].category_uuids
        game = self.api_games.search_game_by_uuid(game_uuid)
        assert game_uuid == game.uuid
        assert game_title == game.title
        assert game_price == game.price
        assert game_category_uuids == game.category_uuids

    @allure.title("Получение списка игр по категории - API-10")
    def test_get_game_by_category(self):
        all_categories = self.api_categories.get_categories_list()
        uuid_category = all_categories.categories[0].uuid
        print(uuid_category)
        game_list_by_category = self.api_categories.get_game_list_by_categories(uuid_category)
        print(game_list_by_category)
        assert [game.category_uuids == uuid_category for game in game_list_by_category.games]# проверяем что в каждой игру uuid category равна uuid category по котороый мы искали игры
















    # @allure.title("Gjkextybt   пользователя по uuid - 'API-1'")
    # def test_get_user_by_uuid1(self, create_user1):
    #     tt=self.api_users.get_user_by_uuid({create_user1})
    #     print(tt["email"])

        # user = self.api_users.create_user()
        # self.api_users.delete_user_by_uuid(user.uuid)