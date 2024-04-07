import requests
import pytest
from colorama import Style, Fore


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


def add_object(name):
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
        json=body).json()
    yield response['id']  # для работы постусловия используем yield
    print("Deleting the post")  # вывести сообщение
    requests.delete(f'https://api.restful-api.dev/objects/{add_object}')  # вывести сообщение


@pytest.fixture()  # Указываем фикстуру... она будет выполниться в выбратых теста, как предусловие
def add_object_fix():
    body = {
        "name": "Apple MacBook Pro DKA",
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
    yield response['id']  # для работы постусловия используем yield
    print("Deleting the post")  # вывести сообщение
    requests.delete(f'https://api.restful-api.dev/objects/{add_object}')  # вывести сообщение


@pytest.mark.parametrize("name", ['DKA_1', 'DKA_2', 'DKA_3', 'DKA_4'])
def test_change_name(name, hello_funk, bef_aft_funk):
    add_object(name)
    print(f"Create object {name}")


def test_change_object_put(add_object_fix, bef_aft_funk):
    new_name = "Apple MacBook Pro 16DKA_PUT"
    body = {
        "name": f"{new_name}"
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{add_object_fix}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect object name"


@pytest.mark.medium  # пометил как medium test (пример вызова pytest -v -m medium)
def test_change_object_patch(add_object_fix, bef_aft_funk):
    new_name = "Apple MacBook Pro 16DKA_Patch"
    body = {
        "name": f"{new_name}",
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{add_object_fix}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect object name"
