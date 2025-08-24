import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_user(new_user):
    resp = requests.get(f"{BASE_URL}/user/{new_user['username']}")
    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == new_user["id"]
    assert body["username"] == new_user["username"]
    assert body["firstName"] == "John"


def test_delete_user(new_user):
    # удаляем пользователя
    resp = requests.delete(f"{BASE_URL}/user/{new_user['username']}")
    assert resp.status_code == 200

    # проверяем, что его больше нет
    resp = requests.get(f"{BASE_URL}/user/{new_user['username']}")
    assert resp.status_code == 404
