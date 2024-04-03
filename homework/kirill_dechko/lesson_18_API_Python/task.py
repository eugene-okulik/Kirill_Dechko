import requests


def add_object():
    body = {
        "name": "Apple MacBook Pro 16DKA",
        "data": {
            "year": 1982,
            "price": 2805.99,
            "CPU model": "Intel Core i9DKA",
            "Hard disk size": "1 TBDKA"
        }
    }
    response = requests.post(  # Ответ равен...
        'https://api.restful-api.dev/objects',
        json=body).json()
    return response['id']


def change_object_put():
    obj_id = add_object()
    new_name = "Apple MacBook Pro 16DKA_PUT"
    body = {
        "name": f"{new_name}"
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect objekt name"


change_object_put()


def change_object_patch():
    obj_id = add_object()
    new_name = "Apple MacBook Pro 16DKA_Patch"
    body = {
        "name": f"{new_name}",
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect objekt name"


change_object_patch()


def object_del(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    print(response)


object_del(add_object())
