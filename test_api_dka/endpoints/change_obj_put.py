import allure
import requests
from endpoints.parent_eadpoint import ParentEndpoint


class ChangeObjectPut(ParentEndpoint):
    """Cоздаем класс для нашего метода PUT, внутри передаем родительский класс
       теперь проверки по созданию, удалению объекта и атрибуты родительского класса (url)
       будут применены при создании объекта"""
    @allure.step('Изменяем существующий объект PUT.')
    def change_obj_put(self, body, obj_id):
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=body
        )
        self.obj_json = self.response.json()
        assert self.response.status_code == 200, f"Object with id {obj_id} wasn't created"
        return self.obj_json['id']
