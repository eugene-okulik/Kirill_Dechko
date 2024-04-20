import pytest
import allure
TEST_DATA = [
    {"name": 'DKA_1', "data": {"year": 1982, "price": 2805.99, "CPU model": "Intel Core i9DKA",
                               "Hard disk size": "1 TB DKA"}},
    {"name": 'DKA_2', "data": {"year": 1982, "price": 2805.99, "CPU model": "Intel Core i9DKA",
                               "Hard disk size": "1 TB DKA"}},
    {"name": 'DKA_3', "data": {"year": 1982, "price": 2805.99, "CPU model": "Intel Core i9DKA",
                               "Hard disk size": "1 TB DKA"}},
    {"name": 'DKA_4', "data": {"year": 1982, "price": 2805.99, "CPU model": "Intel Core i9DKA",
                               "Hard disk size": "1 TB DKA"}}
]

test_body = {"name": 'DKA_2.2.1'}


@allure.feature("Создание объектов")
@allure.story("Проверка создания и удаления объектов")
@allure.title("Создаем объект")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Cоздание объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Создание новых объектов User story-10")
@pytest.mark.parametrize("data", TEST_DATA)
def test_create_obj(data, create_new_obj_endpoint, del_obj_by_id_endpoint):
    obj_id = create_new_obj_endpoint.create_new_obj(data)
    create_new_obj_endpoint.check_obj_name(data['name'])
    del_obj_by_id_endpoint.del_obj(obj_id)


@allure.feature("Перезаписать объект")
@allure.story("Проверка возможности полного изменения объектов")
@allure.title("Полное изменение объекта PUT")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Полное изменение объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Полное изменение объекта User story-11")
@pytest.mark.critical  # отметили тест как критический
def test_change_object_put(create_obj, change_obj_endpoint_put):
    change_obj_endpoint_put.change_obj_put(test_body, create_obj)
    change_obj_endpoint_put.check_obj_name(test_body['name'])


@allure.feature("Обновление объекта")
@allure.story("Проверка возможности частичного изменения объектов")
@allure.title("Частичное изменение объекта PATCH")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Частичное изменение объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Частичное изменение объекта User story-12")
@pytest.mark.medium  # отметили тест как medium
def test_change_object_patch(create_obj, change_obj_endpoint_patch):
    change_obj_endpoint_patch.change_obj_patch(TEST_DATA[3], create_obj)
    change_obj_endpoint_patch.check_obj_name(TEST_DATA[3]['name'])


@allure.feature("Удаление объекта")
@allure.story("Проверка возможности удаления объектов")
@allure.title("Удаляем объект")
@allure.testcase("https://okulik.by/kabinet/group?groupId=52", "Удаление объекта (тест кейс)")
@allure.issue("https://okulik.by/kabinet/group?groupId=52", "Удаление объекта User story-13")
@pytest.mark.critical
def test_del_object(create_obj, del_obj_by_id_endpoint):
    del_obj_by_id_endpoint.del_obj(create_obj)
