from locust import task, HttpUser

post_eandpoint = '/objects'
test_body = {"name": "DKA", "data": {"year": 1982, "price": 2805.99, "CPU model": "Intel Core i9DKA",
                                     "Hard disk size": "1 TB DKA"}}
put_body = {"name": "DKA_PUT"}

patch_body = {"name": "DKA_PATCH", "data": {"year": 1982, "price": 2805.99, "CPU model": "Intel Core i9DKA",
                                            "Hard disk size": "1 TB DKA"}}


class PerformanceAPP(HttpUser):
    obj_id = None

    @task(2)
    def create_objects(self):  # создаем объект, для получения id
        response = self.client.post(  # переменная response хранит результат метода post, дальше можно извлекать id
            # из ответа взять id и работать с ним
            post_eandpoint,
            json=test_body
        )
        self.obj_id = response.json()["id"]  # извлекаем id

    @task(4)
    def change_object_put(self):
        self.client.put(
            f'{post_eandpoint}/{self.obj_id}',
            json=put_body
        )

    @task(4)
    def change_object_patch(self):
        self.client.patch(
            f'{post_eandpoint}/{self.obj_id}',
            json=patch_body
        )

    @task(1)
    def delete_object(self):
        self.client.delete(
            f'{post_eandpoint}/{self.obj_id}'
        )
