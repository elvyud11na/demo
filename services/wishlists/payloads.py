from faker import Faker

faker = Faker()

class Payloads:
    def add_item_wishlist(self, game_uuid):
        return {
          "item_uuid": game_uuid
        }

    def remove_item_wishlist(self, game_uuid):
        return {
            "item_uuid": game_uuid
        }

