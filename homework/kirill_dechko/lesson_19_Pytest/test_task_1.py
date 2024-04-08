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
    return response['id']  # для работы постусловия используем yield


@pytest.mark.parametrize("name", ['DKA_1', 'DKA_2', 'DKA_3', 'DKA_4'])
def test_create_obj(name, hello_funk, bef_aft_funk):
    obj_id = add_object(name)
    assert obj_id is not None, f"Object {name} wasn't created"  # проверяем что после создания есть id
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')  # удаляем объект по id
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')  # запрашиваем удаленный id
    assert response.status_code == 404, f"Object {name} wasn't deleted"


@pytest.mark.critical
def test_change_object_put(bef_aft_funk):
    obj_id = add_object("Apple MacBook")
    new_name = "Apple MacBook Pro 16DKA_PUT"
    body = {
        "name": f"{new_name}"
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect object name"
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')  # запрашиваем удаленный id
    assert response.status_code == 404, f"Object {new_name} wasn't deleted"


@pytest.mark.medium
def test_change_object_patch(bef_aft_funk):
    obj_id = add_object("Apple MacBook Pro 16")
    new_name = "Apple MacBook Pro 16DKA_PATCH"
    body = {
        "name": f"{new_name}",
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body).json()
    print(response)
    assert response['name'] == f"{new_name}", "Incorrect object name"
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')  # запрашиваем удаленный id
    assert response.status_code == 404, f"Object {new_name} wasn't deleted"
