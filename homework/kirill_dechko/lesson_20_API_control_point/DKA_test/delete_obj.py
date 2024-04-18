import allure
import requests
from endpoints.parent_eadpoint import ParentEndpoint


class DeleteObject(ParentEndpoint):

    @allure.step('Удаление объекта.')
    def del_obj(self, obj_id):
        self.response = requests.delete(
            f"{self.url}/{obj_id}"
        )
        self.response = requests.get(
            f"{self.url}/{obj_id}")
        assert self.response.status_code == 404, f"Object with id {obj_id} wasn't deleted"
