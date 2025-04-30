import allure
import pytest

from config.base_test import BaseTest



@allure.epic("Games")
class TestGames(BaseTest):

    @allure.title("Получить список всех игры")
    def test_get_all_game(self):
        game_list = self.api_games.get_games_list()
        #game_first_uuid = game_list.games[0].uuid
        game_uuid = [game.uuid for game in game_list.games]
        print(game_uuid)
        #или через цикл for
        # all_uuids = []
        # for game in game_list.games:
        #     all_uuids.append(game.uuid)
        # print(all_uuids)

    @allure.title("Поиск игры по слову")
    @pytest.mark.parametrize(
            "search_word, expected_result", [
             (None, True),
             ("76437$FF", False)
          ])
    def test_task_2(self, search_word, expected_result):
        if expected_result: #если тест позитивеый, то search_word будет равно из строки 34, если негативный то из берется из передаваемых значений
            game_list = self.api_games.get_games_list()
            first_game_title = game_list.games[0].title# название игры Atomic Heart
            print(first_game_title)
            search_word = first_game_title.split(" ")[0].lower()#часть названия игры получтлось atomic
            #print(search_word)
        search_game_by_word = self.api_games.search_game(0, 10, search_word, expected_result)
        # print(search_game_by_word)
        if expected_result:
            assert search_word in search_game_by_word.games[0].title.lower()
        else:
            assert search_game_by_word == None




