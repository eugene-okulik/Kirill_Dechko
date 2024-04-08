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
    print(response['name'])
    return response['id']  # для работы постусловия используем yield


print(add_object("444"))
print("Deleting the post")  # вывести сообщение
requests.delete(f'https://api.restful-api.dev/objects/{add_object}')  # вывести сообщение

