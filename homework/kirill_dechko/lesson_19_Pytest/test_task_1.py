import requests
import pytest
from colorama import Style, Fore
import random


@pytest.fixture(scope="session")  # фикстура которая отработает в начале и в конце сессии
def hello_funk():
    print(Fore.LIGHTMAGENTA_EX + "\nStart testing" + Style.RESET_ALL)
    yield
    print(Fore.LIGHTMAGENTA_EX + "\nTesting completed" + Style.RESET_ALL)


@pytest.fixture()  # фикстура которая отработает в начале и в конце каждого теста
def bef_aft_funk():
    print(Fore.LIGHTYELLOW_EX + "\nbefore test" + Style.RESET_ALL)
    yield
    print(Fore.LIGHTYELLOW_EX + "\nafter test" + Style.RESET_ALL)


@pytest.fixture()  # создание объекта
def create_del_new_obj():  # функция на создание объекта
    body = {
        "name": f"New_obj_{random.randint}",
        "data": {
            "year": 1982,
            "price": 2805.99,
            "CPU model": "Intel Core i9DKA",
            "Hard disk size": "1 TB DKA"
        }
    }
    response = requests.post(  # Ответ равен...
        'https://api.restful-api.dev/objects',
        json=body).json()
    assert response['name'] == f"New_obj_{random.randint}", "Incorrect random int"
    yield response['id']
    requests.delete(f'https://api.restful-api.dev/objects/{create_del_new_obj}')
    response = requests.get(f'https://api.restful-api.dev/objects/{create_del_new_obj}')  # запрашиваем удаленный id
    assert response.status_code == 404, f"New_obj_{random.randint} wasn't deleted"


@pytest.mark.parametrize("name", ['DKA_1', 'DKA_2', 'DKA_3', 'DKA_4'])  # parametrize создает объекты с name из списка
def test_create_obj(name, hello_funk, bef_aft_funk):
    body = {
        "name": name,
        "data": {
            "year": 1982,
            "price": 2805.99,
            "CPU model": "Intel Core i9DKA",
            "Hard disk size": "1 TB DKA"
        }
    }
    response = requests.post(  # Ответ равен...
        'https://api.restful-api.dev/objects',
        json=body).json()  # вызывает функцию add_object и подставляет в нее name
    assert response['name'] == name, f"Object {name} wasn't created"  # проверяем что после создания есть id
    requests.delete(f'https://api.restful-api.dev/objects/{response}')  # удаляем объект по id
    response = requests.get(f'https://api.restful-api.dev/objects/{response}')  # запрашиваем удаленный id
    assert response.status_code == 404, f"Object {name} wasn't deleted"  # проверяем что пришла ошибка


@pytest.mark.critical  # отметили тест как критический
def test_change_object_put(create_del_new_obj,
                           bef_aft_funk):  # PUT полностью заменит объект и его тело, оставит только name
    new_name = "Apple MacBook Pro 16DKA_PUT"  # полностью затираем объект, остается name Apple MacBook Pro 16DKA_PUT
    body = {
        "name": f"{new_name}"  # полностью затираем объект, остается только name Apple MacBook Pro 16DKA_PUT
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{create_del_new_obj}',
        json=body).json()
    assert response['name'] == f"{new_name}", "Incorrect object name"  # проверяем созданное имя


@pytest.mark.medium  # отметили тест как medium
def test_change_object_patch(create_del_new_obj,
                             bef_aft_funk):  # PATCH заменит только name у созданного объекта, остальное не тронет
    new_name = "Apple MacBook Pro 16DKA_PATCH"
    body = {
        "name": f"{new_name}",  # меняем только name
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{create_del_new_obj}',
        json=body).json()
    assert response['name'] == f"{new_name}", "Incorrect object name"  # проверяем измененное имя объекта
