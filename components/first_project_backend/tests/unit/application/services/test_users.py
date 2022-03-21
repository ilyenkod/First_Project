import pytest

from components.first_project_backend.chats.adapters.database.tables import users_base
from components.first_project_backend.chats.application import services


@pytest.fixture(scope='function')
def service(users_repo):
    return services.Users(users_repo=users_repo)

def test_create_user(service):
    user = services.UserInfo(name="Dima", password="123")
    service.create_user(user)
    service.users_repo.create_user.assert_called_once()





