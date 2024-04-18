import requests
import allure
from endpoints.parent_eadpoint import ParentEndpoint


class CreateObject(ParentEndpoint):  # создаем класс для нашего метода POST

    @allure.step('Создаем новый объект.')
    def create_new_obj(self, body):  # создаем метод для создания нового объекта
        self.response = requests.post(  # из self.response можем получить статус-код (прим: <Response [200]>)
            self.url,  # передаем url в метод
            json=body  # передаем body в метод
        )
        self.obj_json = self.response.json()
        self.obj_id = self.obj_json['id']
        return self.obj_id  # возвращаем id, если нужен return
