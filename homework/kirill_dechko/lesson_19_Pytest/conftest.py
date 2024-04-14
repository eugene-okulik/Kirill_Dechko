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
