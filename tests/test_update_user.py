
def test_update_user(users_api):

    user_data = {
        "name": "Aleksandar Updated",
        "job": "Senior QA Engineer"
    }

    response = users_api.update_user(2, user_data)

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == user_data["name"]
    assert body["job"] == user_data["job"]
    assert "updatedAt" in body
