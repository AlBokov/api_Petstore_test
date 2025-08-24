import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_pet(new_pet):
    resp = requests.get(f"{BASE_URL}/pet/{new_pet}")
    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == new_pet
    assert body["name"] == "Rex"
    assert body["status"] == "available"


def test_delete_pet(new_pet):
    # удаляем питомца
    resp = requests.delete(f"{BASE_URL}/pet/{new_pet}")
    assert resp.status_code == 200

    # проверяем, что его больше нет
    resp = requests.get(f"{BASE_URL}/pet/{new_pet}")
    assert resp.status_code == 404