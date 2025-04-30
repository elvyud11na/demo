import os

from config.stages import get_stage

 #импортируем метод get_stage в котором определяется хост в зависимости от стенда


class Endpoints:

    get_users = f"{get_stage()}/users"
    create_user = f"{get_stage()}/users"
    get_user_by_uuid = lambda self, uuid: f"{get_stage()}/users/{uuid}"
    get_user_using_credentials = f"{get_stage()}/users/login" #получить пользователя, используя учетные данные
    update_user = lambda self, uuid: f"{get_stage()}/users/{uuid}"
    delete_user = lambda self, uuid: f"{get_stage()}/users/{uuid}"


#print(Endpoints.get_users)

#вариант 2, без файла stages, прям здесь прписываем условие какой будет хост в зависимости от стенда - мне это вариант больше нравится
# HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "dev" else "https://release-gs.qa-playground.com/api/v1"
#
# class Endpoints:
#     get_users = f"{HOST}/users"
#
#print(Endpoints.get_users)
# пример использования сначало в терминале пишем $env:STAGE="dev"
# потом enter и пишем python services/users/endpoints.py
# резудьтат https://dev-gs.qa-playground.com/api/v1/users
# если ругается ModuleNotFoundError: No module named 'config'
#то пишем
# "$($env:PYTHONPATH);C:\Users\elvyu\PycharmProjects\projectAPI"