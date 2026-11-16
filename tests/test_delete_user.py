
def test_delete_user(users_api):

    response = users_api.delete_user(2)

    assert response.status_code == 204
    assert response.text == ""
