import pytest
from endpoints.create_obj import CreateObject
from endpoints.change_obj_patch import ChangeObjectPatch
from endpoints.change_obj_put import ChangeObjectPut
from endpoints.delete_obj import DeleteObject
from faker import Faker

fake = Faker()


@pytest.fixture()
def create_new_obj_endpoint():
    return CreateObject()


@pytest.fixture()
def change_obj_endpoint_patch():
    return ChangeObjectPatch()


@pytest.fixture()
def change_obj_endpoint_put():
    return ChangeObjectPut()


@pytest.fixture()
def del_obj_by_id_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_obj(create_new_obj_endpoint):
    body = {
        "name": "TEST_DKA_NEW_OBJ_NAME",
        "data": {
            "year": 1982,
            "price": 2805.99,
            "CPU model": "Intel Core i9DKA",
            "Hard disk size": "1 TB DKA"
        }
    }
    create_new_obj_endpoint.create_new_obj(body)
    create_new_obj_endpoint.check_obj_name("TEST_DKA_NEW_OBJ_NAME")
    return create_new_obj_endpoint.obj_id
