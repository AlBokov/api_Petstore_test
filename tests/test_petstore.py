import requests
import pytest
BASE_URL = "https://petstore.swagger.io/v2"


def test_create_pet():
    payload = {"id": 999, "name": "Rex", "status": "available"}
    resp = requests.post(f"{BASE_URL}/pet", json=payload)

    assert resp.status_code == 200


def test_get_a_pet():
    resp = requests.get(F"{BASE_URL}/pet/999")

    assert resp.status_code == 200
    assert resp.json()["name"] == "Rex"


def test_delete_pet():
    resp = requests.delete(f"{BASE_URL}/pet/999")
    assert resp.status_code == 200

def test_create_users():
    payload = {
  "id": 1,
  "username": "Alex",
  "firstName": "Admin",
  "lastName": "Smok",
  "email": "test@mail.ru",
  "password": "23456",
  "phone": "89436748234",
  "userStatus": 0
}
    resp = requests.post(f"{BASE_URL}/user", json=payload)
    assert resp.status_code == 200


def test_get_a_user():
    resp = requests.get(f"{BASE_URL}/user/Alex")
    assert resp.status_code == 200
    assert resp.json()["id"] == 1


def test_delete_user():
    resp = requests.delete(f"{BASE_URL}/user/Alex")
    assert resp.status_code == 200



