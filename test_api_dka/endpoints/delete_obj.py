import allure
import requests
from endpoints.parent_eadpoint import ParentEndpoint


class DeleteObject(ParentEndpoint):
    """Cоздаем класс для нашего метода DELETE, внутри передаем родительский класс
       теперь проверки по созданию, удалению объекта и атрибуты родительского класса (url)
       будут применены при создании объекта"""
    @allure.step('Удаление объекта.')
    def del_obj(self, obj_id):
        self.response = requests.delete(
            f"{self.url}/{obj_id}"
        )
        self.response = requests.get(
            f"{self.url}/{obj_id}")
        assert self.response.status_code == 404, f"Object with id {obj_id} wasn't deleted"
