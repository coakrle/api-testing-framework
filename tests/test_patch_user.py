
def test_patch_user(users_api):

    user_data = {
        "job": "QA Automation Engineer"
    }

    response = users_api.patch_user(2, user_data)

    assert response.status_code == 200

    body = response.json()

    assert body["job"] == user_data["job"]
    assert "updatedAt" in body
