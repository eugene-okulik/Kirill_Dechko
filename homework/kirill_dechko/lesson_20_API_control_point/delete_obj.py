import allure
import requests


class DeleteObject:
    url = 'https://api.restful-api.dev/objects'
    response = None  # изначально он пустой, заполнится после отработки create_new_object
    obj_json = None

    @allure.step('Удаление объекта.')
    def del_obj(self, obj_id):
        self.response = requests.delete(
            f"{self.url}/{obj_id}"
        )
        self.response = requests.get(
            f"{self.url}/{obj_id}")
        assert self.response.status_code == 404, f"Object with id {obj_id} wasn't deleted"
