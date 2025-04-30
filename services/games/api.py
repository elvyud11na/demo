import requests
import allure

from services.games.models.model_game import GamesModel
from services.games.models.model_one_game import GameModel
from utils.helper import Helper
from config.headers import Headers
from services.games.endpoints import Endpoints
from services.games.payloads import Payloads



class GameslistAPI(Helper):

    def __init__(self):
        self._payloads = Payloads()
        self._endpoints = Endpoints()
        self._headers = Headers()

    @allure.step("Get games")
    def get_games_list(self, offset=0, limit=10, expected_result=True) -> GamesModel:
        response = requests.get(
            url=self._endpoints.all_games,
            headers=self._headers.basic,
            params={
                "offset": offset,
                "limit": limit
            },
            verify=False
        )
        if expected_result:
            assert response.status_code == 200, response.json()
            model = GamesModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()
        self.attach_response(response.json())

    @allure.step("Search game by name")
    def search_game(self, offset=0, limit=10, search_word="atomic", expected_result=True) -> GamesModel:
        response = requests.get(
            url=self._endpoints.search_game,
            headers=self._headers.basic,
            params={
                "offset": offset,
                "limit": limit,
                "query": search_word
            },
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = GamesModel(**response.json())
            return model
        else:
            assert response.status_code == 200, response.json()

    @allure.step("Search game by uuid")
    def search_game_by_uuid(self, game_uuid, expected_result=True) -> GameModel:
        response = requests.get(
            url=self._endpoints.search_game_by_uuid(game_uuid),
            headers=self._headers.basic,
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = GameModel(**response.json())
            return model
        else:
            assert response.status_code == 200, response.json()

    # def get_game_uuid(self):
    #     def inner_function(get_games_list):
    #         game_list = get_games_list.get_games_list()
    #         all_uuids = [game.uuid for game in game_list]
    #         return all_uuids
    #     return inner_function
    # в тесте надо  def test_test(self):
    #         instance = GameslistAPI()
    #         game_uuids = instance.get_game_uuid()(instance)
    #         print(game_uuids)

