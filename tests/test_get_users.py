import pytest

def test_get_users(users_api):

    response = users_api.get_users()

    assert response.status_code == 200

    body = response.json()

    assert body["page"] == 2
    assert len(body["data"]) == 6

    first_user = body["data"][0]

    assert "id" in first_user
    assert "email" in first_user
    assert "first_name" in first_user
    assert "last_name" in first_user

def test_get_single_user(users_api):

    response = users_api.get_user(2)

    assert response.status_code == 200

    body = response.json()
    user = body["data"]

    assert user["id"] == 2
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user



@pytest.mark.parametrize("user_id", [9999, 99999, 0])
def test_get_non_existing_user(users_api, user_id):

    response = users_api.get_user(user_id)

    assert response.status_code == 404

    body = response.json()

    assert body == {}



def test_get_user_with_invalid_id(users_api):

    response = users_api.get_user("invalid")

    assert response.status_code == 404

    body = response.json()

    assert body == {}
