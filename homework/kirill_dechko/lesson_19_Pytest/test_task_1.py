import requests
import pytest
import allure


@allure.feature("Создание объектов")
@allure.story("Проверка создания и удаления объектов")
@allure.title("Создаем объект")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Cоздание объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Создание новых объектов User story-10")
@pytest.mark.parametrize("name", ['DKA_1', 'DKA_2', 'DKA_3', 'DKA_4'])  # parametrize создает объекты с name из списка
def test_create_obj(name, hello_funk, bef_aft_funk):
    with allure.step('Создаем тестовые данные'):  # Уточняем для красоты и понимания, что делают блоки кода
        body = {
            "name": name,
            "data": {
                "year": 1982,
                "price": 2805.99,
                "CPU model": "Intel Core i9DKA",
                "Hard disk size": "1 TB DKA"
            }
        }
    with allure.step('Отправляем запрос на создание объекта'):
        response = requests.post(  # Ответ равен...
            'https://api.restful-api.dev/objects',
            json=body).json()  # вызывает функцию add_object и подставляет в нее name
    assert response['name'] == name, f"Object {name} wasn't created"  # проверяем что после создания есть id
    with allure.step('Отправляем запрос на удаление объекта'):
        requests.delete(f'https://api.restful-api.dev/objects/{response}')  # удаляем объект по id
    with allure.step('Проверяем отсутствие объекта'):
        response = requests.get(f'https://api.restful-api.dev/objects/{response}')  # запрашиваем удаленный id
    assert response.status_code == 404, f"Object {name} wasn't deleted"  # проверяем что пришла ошибка


@allure.feature("Перезаписать объект")
@allure.story("Проверка возможности полного изменения объектов")
@allure.title("Изменяем объект")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Полное изменение объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Полное изменение объекта User story-11")
@pytest.mark.critical  # отметили тест как критический
def test_change_object_put(create_del_new_obj,
                           bef_aft_funk):  # PUT полностью заменит объект и его тело, оставит только name
    with allure.step("Подготовка данных"):
        new_name = "Apple MacBook Pro 16DKA_PUT"  # полностью затираем объект, остается name Apple MacBook Pro 16DKA_PUT
        body = {
            "name": f"{new_name}"  # полностью затираем объект, остается только name Apple MacBook Pro 16DKA_PUT
        }
    with allure.step("Отправка PUT запроса на изменение данных"):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{create_del_new_obj}',
            json=body).json()
    assert response['name'] == f"{new_name}", "Incorrect object name"  # проверяем созданное имя


@allure.feature("Обновление объекта")
@allure.story("Проверка возможности частичного изменения объектов")
@allure.title("Изменяем объект")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Частичное изменение объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Частичное изменение объекта User story-12")
@pytest.mark.medium  # отметили тест как medium
def test_change_object_patch(create_del_new_obj,
                             bef_aft_funk):  # PATCH заменит только name у созданного объекта, остальное не тронет
    with allure.step("Подготовка данных"):
        new_name = "Apple MacBook Pro 16DKA_PATCH"
        body = {
            "name": f"{new_name}",  # меняем только name
        }
    with allure.step("Отправка POST запроса на изменение данных"):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{create_del_new_obj}',
            json=body).json()
    assert response['name'] == f"{new_name}", "Incorrect object name"  # проверяем измененное имя объекта


@allure.feature("Удаление объекта")
@allure.story("Проверка возможности удаления объектов")
@allure.title("Удаляем объект")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Удаление объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Удаление объекта User story-13")
@pytest.mark.critical
def test_del_obj(create_del_new_obj, bef_aft_funk):
    with allure.step("Отправка DELETE запроса на удаление данных"):
        requests.delete(f'https://api.restful-api.dev/objects/{create_del_new_obj}')  # удаляем объект по id
    with allure.step("Отправка GET запроса на получение удаленных данных"):
        response = requests.get(f'https://api.restful-api.dev/objects/{create_del_new_obj}')  # запрашиваем удаленный id
    assert response.status_code == 404, f"Object with id {create_del_new_obj} wasn't deleted"
