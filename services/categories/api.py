import requests
import allure

from services.categories.models.model_all_categories import AllCategoriesModel
from services.categories.models.model_games_by_category import GamesByCategoryModel
#from services.categories.models.model_categories import CategoriesModel
from utils.helper import Helper
from config.headers import Headers
from services.categories.endpoints import Endpoints
from services.categories.payloads import Payloads



class CategorieslistAPI(Helper):

    def __init__(self):
        self._payloads = Payloads()
        self._endpoints = Endpoints()
        self._headers = Headers()

    @allure.step("Get categories")
    def get_categories_list(self, offset=0, limit=10, expected_result=True) -> AllCategoriesModel:
        response = requests.get(
            url=self._endpoints.get_categories,
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
            model = AllCategoriesModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()



    @allure.step("Search game by uuid")
    def get_game_list_by_categories(self, category_uuid, expected_result=True) -> GamesByCategoryModel:
        response = requests.get(
            url=self._endpoints.game_list_by_categories(category_uuid),
            headers=self._headers.basic,
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = GamesByCategoryModel(**response.json())
            return model
        else:
            assert response.status_code == 200, response.json()

