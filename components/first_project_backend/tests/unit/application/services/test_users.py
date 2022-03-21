import pytest

from components.first_project_backend.chats.adapters.database.tables import users_base
from components.first_project_backend.chats.application import services


@pytest.fixture(scope='function')
def service(users_repo):
    return services.Users(users_repo=users_repo)

def test_create_user(service):
    user = services.UserInfo(name="Dima", password="123")
    firt_len = len(users_base)
    service.create_user(user)
    second_len = len(users_base)
    assert second_len == firt_len + 1




