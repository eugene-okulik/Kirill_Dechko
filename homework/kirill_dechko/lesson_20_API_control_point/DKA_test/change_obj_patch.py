import allure
import requests
from endpoints.parent_eadpoint import ParentEndpoint


class ChangeObjectPatch(ParentEndpoint):

    @allure.step('Изменяем существующий объект.')
    def change_obj_patch(self, body, obj_id):
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=body
        )
        self.obj_json = self.response.json()
        return self.obj_json['id']
