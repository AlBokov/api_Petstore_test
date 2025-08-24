import pytest
import requests
import random

BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture
def new_pet():
    """Создание нового питомца перед тестом и удаление после"""
    pet_id = random.randint(1000, 9999)
    payload = {"id": pet_id, "name": "Rex", "status": "available"}
    resp = requests.post(f"{BASE_URL}/pet", json=payload)
    assert resp.status_code == 200
    yield pet_id
    requests.delete(f"{BASE_URL}/pet/{pet_id}")


@pytest.fixture
def new_user():
    """Создание нового пользователя перед тестом и удаление после"""
    username = f"user_{random.randint(1000, 9999)}"
    payload = {
        "id": random.randint(1000, 9999),
        "username": username,
        "firstName": "John",
        "lastName": "Doe",
        "email": "test@mail.com",
        "password": "12345",
        "phone": "1234567890",
        "userStatus": 0
    }
    resp = requests.post(f"{BASE_URL}/user", json=payload)
    assert resp.status_code == 200
    yield payload
    requests.delete(f"{BASE_URL}/user/{username}")
