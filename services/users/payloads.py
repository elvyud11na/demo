from faker import Faker

faker = Faker()

class Payloads:

    def create_user_payload(self):
        return {
          "email": faker.email(),
          "password": "wqwewewr1!!",
          "name": faker.first_name(),
          "nickname": faker.user_name()
        }
    def get_user_using_credentials(self, email, password):
        return {
                "email": email,
                "password": password
            }
    def update_user(self, email, name, nickname):
        return {
              "email": email,
              "name": name,
              "password": "password",
              "nickname": nickname
            }

