
import pytest
import requests
from utils.config import BASE_URL


@pytest.mark.parametrize(
    "api_key",
    [
        "invalid-api-key",
        "12345"
    ]
)
def test_get_users_with_invalid_api_key(api_key):

    headers = {
        "x-api-key": api_key
    }

    response = requests.get(
        f"{BASE_URL}/api/users?page=2",
        headers=headers
    )

    assert response.status_code in (401, 403)


