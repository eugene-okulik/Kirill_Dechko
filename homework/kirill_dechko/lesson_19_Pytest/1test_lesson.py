import requests
import pytest
import random


@pytest.fixture(scope='session')  # фикстура которая отработает для всей сессии
def hello():
    print('Start testing')
    yield
    print('Bye!')


@pytest.fixture()  # Указываем фикстуру... она будет выполниться в выбратых тестак, как предусловие
def add_object():
    body = {
        "name": f"Apple MacBook Pro DKA",
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
    yield response['id']  # для работы постусловия используем yield
    print("Deleting the post")  # вывести сообщение
    requests.delete(f'https://api.restful-api.dev/objects/{add_object}')  # вывести сообщение


def test_change_object_put(add_object, hello):
    new_name = "Apple MacBook Pro 16DKA_PUT"
    body = {
        "name": f"{new_name}"
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{add_object}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect objekt name"


def test_change_object_patch(add_object):
    new_name = "Apple MacBook Pro 16DKA_Patch"
    body = {
        "name": f"{new_name}",
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{add_object}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect objekt name"



# def test_object_del(add_object):
#     response = requests.delete(f'https://api.restful-api.dev/objects/{add_object}')
#     print(response)

