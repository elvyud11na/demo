import os
from dotenv import load_dotenv
load_dotenv()

# если токен динамичный, то мы не можем его прописать в фикстуре
# # conftest.py
# @pytest.fixture(scope="session")
# def user_token(): # Фикстура, которая устанавливает токен
#     os.environ["USER_TOKEN"] = "QWERTY"
# Далее вы захотите использовать эту переменную, допустим в файле headers.py
# headers.py
#
# class Headers:
#
#     token = os.getenv("USER_TOKEN")
#
# А затем прокинуть в тест:
# test_example.py
# from data.headers import Headers
#
# class TestExample:
#
#     def test_example(self):
#         print(Headers.token) # None
# Ничего не выйдет, вы получите None. Потому что фикстура установит переменную
# окружения в контексте тестов и все! Соответственно в этом случае, логику получения
# и установки переменной нужно вынести в файл, в котором она нужна.
# В нашем случае headers.py
# # headers.py
#
# import os
#
# def get_user_token(): # Функция получения и установки токена
#      прописываем как получаем токен и записываем его в переменную
#     os.environ["USER_TOKEN"] = "QWERTY"
#
# get_user_token() # Вызов функции для установки токена глобально
#
# class Headers:
#
#     basic = {
#         "Authorization": f"Bearer {os.getenv('USER_TOKEN')}",
#         "X-Task-Id": "API-1"
#     }
# print(Headers.token) # QWERTY
# Вот теперь, токен будет доступен ив тесте путем импорта headers
# # test_example.py
#
# from data.headers import Headers
#
# class TestExample:
#
#     def test_example(self):
#         print(Headers.token) # QWERTY

class Headers:

#     def basic(self, xtask):
#         return {
#             "Authorization": f"Bearer {os.getenv('TOKEN')}",
#             "X-Task-Id": f"{xtask}"
#         }
#
# headers = Headers()
# print(headers.basic("API-1"))
    basic = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}", # если токен статичный, мы его просто записываем в .env и отдуда подставляем сюда
        "X-Task-Id": "API-1"
    }

#print(Headers.basic)