import allure
import requests


class ParentEndpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    obj_json = None

    @allure.step('Проверяем имя созданного объекта.')
    def check_obj_name(self, name):
        assert self.obj_json['name'] == name, f"Object {name} wasn't created."

    @allure.step('Удаление объекта.')
    def del_obj(self):
        self.response = requests.delete(
            f"{self.url}/{self.obj_json['id']}"
        )
        self.response = requests.get(
            f"{self.url}/{self.obj_json['id']}")
        assert self.response.status_code == 404, f"Object with id {self.obj_json['id']} wasn't deleted"

