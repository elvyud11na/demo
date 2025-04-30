import os


def get_stage():
    stages = {
      "dev": "https://dev-gs.qa-playground.com/api/v1",
      "release": "https://release-gs.qa-playground.com/api/v1"
    }

    STAGE = stages[os.environ["STAGE"]] #API урок 4 (архитектура часть 1 - 31-я минута пояснение)
                                        # мы пишем в строке 10, что STAGE = stages из строки 5, а ключ передаем через os.environ["STAGE"]
    return STAGE



#для проверки
#print(get_stage())
# в терминале
# (.venv) PS C:\Users\elvyu\PycharmProjects\projectAPI>$env:STAGE="release"
# (.venv) PS C:\Users\elvyu\PycharmProjects\projectAPI> python config/stages.py



