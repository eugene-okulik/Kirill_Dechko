import allure
import requests
from endpoints.parent_eadpoint import ParentEndpoint


class ChangeObjectPatch(ParentEndpoint):
    """Cоздаем класс для нашего метода PATCH, внутри передаем родительский класс
   теперь проверки по созданию, удалению объекта и атрибуты родительского класса (url)
   будут применены при создании объекта"""
    @allure.step('Изменяем существующий объект.')
    def change_obj_patch(self, body, obj_id):
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=body
        )
        self.obj_json = self.response.json()
        assert self.response.status_code == 200, f"Object with id {obj_id} wasn't created"
        return self.obj_json['id']
