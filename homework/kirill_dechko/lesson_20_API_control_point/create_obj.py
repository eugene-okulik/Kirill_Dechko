import requests
import allure

from endpoints.parent_eadpoint import ParentEndpoint


class CreateObject(ParentEndpoint):  # создаем класс для нашего метода POST
    # url = 'https://api.restful-api.dev/objects'  # указываем общие черты каждого теста URL
    # response = None  # изначально он пустой, заполнится после отработки create_new_object
    # obj_json = None
    # obj_id = None

    # def __init__(self):
    #     self.response = None
    #     self.obj_json = None
    #     self.obj_id = None

    @allure.step('Создаем новый объект.')
    def create_new_obj(self, body):  # создаем метод для создания нового объекта
        self.response = requests.post(  # из self.response можем получить статус-код (прим: <Response [200]>)
            self.url,  # передаем url в метод
            json=body  # передаем body в метод
        )
        self.obj_json = self.response.json()
        self.obj_id = self.obj_json['id']
        return self.obj_id  # возвращаем id, если нужен return

    # @allure.step('Проверяем имя созданного объекта.')
    # def check_obj_name(self, name):
    #     assert self.obj_json['name'] == name, f"Object {name} wasn't created."
    #
    # @allure.step('Удаление объекта.')
    # def del_obj(self):
    #     self.response = requests.delete(
    #         f"{self.url}/{self.obj_json['id']}"
    #     )
    #     self.response = requests.get(
    #         f"{self.url}/{self.obj_json['id']}")
    #     assert self.response.status_code == 404, f"Object with id {self.obj_json['id']} wasn't deleted"
