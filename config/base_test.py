from services.categories.api import CategorieslistAPI
from services.games.api import GameslistAPI
from services.users.api import UsersAPI
from services.wishlists.api import WishlistsAPI
from utils.helper import Helper



class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_wishlist = WishlistsAPI()
        self.api_games = GameslistAPI()
        self.api_categories= CategorieslistAPI()