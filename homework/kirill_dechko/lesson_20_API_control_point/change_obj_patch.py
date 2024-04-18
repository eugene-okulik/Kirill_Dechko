import allure
import requests


class ChangeObjectPatch:
    url = 'https://api.restful-api.dev/objects'
    response = None
    obj_json = None

    @allure.step('Изменяем существующий объект.')
    def change_obj_patch(self, body, obj_id):
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=body
        )
        self.obj_json = self.response.json()
        return self.obj_json['id']

    @allure.step('Проверяем имя измененного объекта.')
    def check_obj_name(self, name):
        assert self.obj_json['name'] == name, f"Object {name} wasn't created."

