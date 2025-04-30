
from config.stages import get_stage

class Endpoints:
    get_user_by_uuid = lambda self, uuid: f"{get_stage()}/users/{uuid}/wishlist"
    add_item_wishlist = lambda self, uuid: f"{get_stage()}/users/{uuid}/wishlist/add"
    remove_item_wishlist = lambda self, uuid: f"{get_stage()}/users/{uuid}/wishlist/remove"