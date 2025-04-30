import requests
import allure
from utils.helper import Helper
from config.headers import Headers
from services.wishlists.endpoints import Endpoints
from services.wishlists.payloads import Payloads

from services.wishlists.models.model_users_wishlist import UsersWishlistModel


class WishlistsAPI(Helper):

    def __init__(self):

        self._payloads = Payloads()
        self._endpoints = Endpoints()
        self._headers = Headers()

    @allure.step("Get user's wishlist")
    def get_users_wishlist_by_uuid(self, uuid, expected_result=True) -> UsersWishlistModel:
        response = requests.get(
            url=self._endpoints.get_user_by_uuid(uuid),
            headers=self._headers.basic,
            verify=False
        )
        model = self.validate_response(
            response=response,
            model=UsersWishlistModel,
            status_code=200,
            expected_result=expected_result
        )
        return model

        # if expected_result:
        #     assert response.status_code == 200, response.json()
        #     model = UsersWishlistModel(**response.json())
        #     return model
        # else:
        #     assert response.status_code != 200, response.json()
        # self.attach_response(response.json())

    @allure.step("Add an item to wishlist")
    def add_item_wishlist(self, uuid, game_uuid, expected_result=True) -> UsersWishlistModel:
        response = requests.post(
            url=self._endpoints.add_item_wishlist(uuid),
            headers=self._headers.basic,
            json=self._payloads.add_item_wishlist(game_uuid),
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UsersWishlistModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()
        self.attach_response(response.json())


    @allure.step("Remove an item to wishlist")
    def remove_item_wishlist(self, uuid, game_uuid, expected_result=True) -> UsersWishlistModel:
        response = requests.post(
            url=self._endpoints.remove_item_wishlist(uuid),
            headers=self._headers.basic,
            json=self._payloads.remove_item_wishlist(game_uuid),
            verify=False
        )
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == 200, response.json()
            model = UsersWishlistModel(**response.json())
            return model
        else:
            assert response.status_code != 200, response.json()
        self.attach_response(response.json())
