from faker import Faker

faker = Faker()

class Payloads:
    def add_item_wishlist(self, item_uuid):
        return {
          "item_uuid": item_uuid
        }

