import allure

from config.base_test import BaseTest

@allure.epic("Users")
class TestUsersWishlist(BaseTest):

    @allure.step("Get wishlist by uuid user")
    def test_get_wishlist_by_uuid_user(self):
        user = self.api_users.create_user()
        self.api_wishlist.get_users_wishlist_by_uuid(user.uuid)




    @allure.step("Add an item to wishlist")
    def test_add_item_wishlist_for_new_user(self):
        user = self.api_users.create_user()
        game_list = self.api_games.get_games_list()
        game_first_game_uuid = game_list.games[0].uuid
        print(game_first_game_uuid)
        print(str(game_first_game_uuid))
        self.api_wishlist.add_item_wishlist(uuid=user.uuid, item_uuid=game_first_game_uuid)
        user_wishlist = self.api_wishlist.get_users_wishlist_by_uuid(user.uuid)
        print(user_wishlist)
        print(user_wishlist.items[0].uuid)
        assert str(user_wishlist.items[0].uuid) == str(game_first_game_uuid) # UUIDs хранятся в формате Base64, поэтому их надо преобразовать в строку
        uuid_games = any(str(item.uuid) == str(game_first_game_uuid) for item in user_wishlist.items)
        assert uuid_games == True


    #
    # @allure.step("Добавление игры в список желаемого юзера 'API-5'")
    # def test_api_1(self):
    #     all_users = self.api_users.get_all_users()
    #     user_uuid = all_users.users[2].uuid
    #     wishlist_user_before = self.api_wishlist.get_users_wishlist_by_uuid(user_uuid)
    #     game_list = self.api_games.get_games_list()
    #     game_uuid = [game.uuid for game in game_list.games]
    #     print(game_uuid)
    #     game_uuid_last = game_uuid[0]
    #     print(game_uuid_last)
    #     self.api_wishlist.add_item_wishlist(user_uuid, game_uuid_last)
    #     wishlist_user_after = self.api_wishlist.get_users_wishlist_by_uuid(user_uuid)
    #     print(wishlist_user_after)
    #     print(f"{wishlist_user_after.items[-1].uuid}")
    #     assert f"{wishlist_user_after.items[-1].uuid}" == game_uuid_last
    #     assert wishlist_user_before != wishlist_user_after



        # user_not_exists = any(element.uuid == user_wishlist.user_uuid for element in game_list.games)
        # user_not_exists == True

        # all_users = self.api_users.get_all_users()
        # print(f"UUID первого юзера: {all_users.users[0].uuid}")
        #game_list = self.api_games.get_games_list()
        # game_first_uuid = game_list.games[0].uuid
        # print(game_first_uuid)
        # game_uuid = [game.uuid for game in game_list.games]
        # print(game_uuid)
