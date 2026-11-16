
def test_create_user(users_api):

    user_data = {
        "name": "Aleksandar",
        "job": "QA Engineer"
    }

    response = users_api.create_user(user_data)

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == user_data["name"]
    assert body["job"] == user_data["job"]
    assert "id" in body
    assert "createdAt" in body



def test_create_user_with_empty_data(users_api):

    user_data = {}

    response = users_api.create_user(user_data)

    assert response.status_code == 201

    body = response.json()

    assert "id" in body
    assert "createdAt" in body


import requests
from utils.config import BASE_URL, API_KEY


def test_create_user_with_invalid_json():

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{BASE_URL}/api/users",
        headers=headers,
        data="{invalid json}"
    )

    assert response.status_code == 400
