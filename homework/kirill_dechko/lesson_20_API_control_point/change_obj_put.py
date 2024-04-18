import allure
import requests


class ChangeObjectPut:
    url = 'https://api.restful-api.dev/objects'
    response = None
    obj_json = None
    obj_id = None

    @allure.step('Изменяем существующий объект Put.')
    def change_obj_put(self, body, obj_id):
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=body
        )
        self.obj_json = self.response.json()
        return self.obj_json['id']

    @allure.step('Проверяем имя измененного объекта.')
    def check_obj_name(self, name):
        assert self.obj_json['name'] == name, f"Object {name} wasn't created."
