import allure


class ParentEndpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    obj_json = None

    @allure.step('Проверяем имя созданного объекта.')
    def check_obj_name(self, name):
        assert self.obj_json['name'] == name, f"Object {name} wasn't created."
