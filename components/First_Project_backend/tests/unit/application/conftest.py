import pytest
from unittest.mock import Mock

from components.First_Project_backend.chats.application import interfaces
from components.First_Project_backend.chats.adapters.database import repositories

@pytest.fixture(scope='function')
def users_repo():
    users_repo = repositories.UsersRepo()
    return users_repo

@pytest.fixture(scope='function')
def chats_repo():
    chats_repo = repositories.ChatsRepo()
    return chats_repo



