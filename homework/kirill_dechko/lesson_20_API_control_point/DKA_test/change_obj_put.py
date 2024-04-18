import allure
import requests
from endpoints.parent_eadpoint import ParentEndpoint


class ChangeObjectPut(ParentEndpoint):

    @allure.step('Изменяем существующий объект Put.')
    def change_obj_put(self, body, obj_id):
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=body
        )
        self.obj_json = self.response.json()
        return self.obj_json['id']
