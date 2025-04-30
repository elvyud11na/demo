# import allure
# import json
#
#
# class Helper:
#
#     def attach_response(self, response):
#         response = json.dumps(response, indent=4)
#         allure.attach(body=response, name="API Response", attachment_type=allure.attachment_type.JSON)



import json
import allure
import requests
from pydantic import BaseModel
from config.headers import Headers
class Helper:
    def attach_response(self, response):
        result = json.dumps(response, indent=4)
        allure.attach(
            body=result,
            name="API response",
            attachment_type=allure.attachment_type.JSON
        )

    def validate_response(self, response: requests.Response, model: type[BaseModel], status_code: int = 200,
                          expected_result: bool = True):
        self.attach_response(response.json())
        if expected_result:
            assert response.status_code == status_code, response.json()
            if isinstance(response.json(), dict): #проверяем что  если response.json() является dict, тогда возвращаем model(**response.json())
                return model(**response.json())
            elif isinstance(response.json(), list):
                return [model(**item) for item in response.json()]
        else:
            assert response.status_code != 200, response.json()


    # def assert_status_code(self, status_code: int = 200):
    #     assert self.response.status_code == status_code, self.response.json()