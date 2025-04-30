import pytest
import requests
from dotenv import load_dotenv
from config.stages import get_stage

from faker import Faker
from config.headers import Headers
from services.users.endpoints import Endpoints
#
#
#
# load_dotenv()
# @pytest.fixture(autouse=True, scope="session")
# def init_environment():
#     response = requests.post(
#         url=f"{get_stage()}/setup",
#         headers=Headers().basic
#     )
#     assert response.status_code == 205#
#
#
faker = Faker()
#фикстура которая создает пользователя, а пот его удалет
@pytest.fixture()
def create_user():
    fake = Faker()
    data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.first_name(),
        "nickname": fake.user_name()
    }
    response = requests.post(
        url=Endpoints.create_user,
        headers=Headers.basic,
        json=data,
        verify=False
    )
    if response.status_code != 200:
        raise ValueError("User creation failed with status code {}".format(response.json()))
    uuid = response.json()['uuid']
    #print(uuid)
    yield uuid
    requests.delete(
        url=f"{get_stage()}/users/{uuid})",
        headers=Headers.basic,
        verify=False
    )
    if response.status_code != 200:
        raise ValueError("User delete failed with status code {}".format(response.json()))

