
import pytest
from api.users_api import UsersAPI


@pytest.fixture
def users_api():
    api = UsersAPI()

    yield api

    api.close()

