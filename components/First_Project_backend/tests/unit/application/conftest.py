import pytest
from unittest.mock import Mock

from components.First_Project_backend.chats.application import interfaces, services
from components.First_Project_backend.chats.adapters.database import repositories

@pytest.fixture(scope='function')
def users_repo():
    users_repo = repositories.UsersRepo()
    return users_repo

@pytest.fixture(scope='function')
def chats_repo():
    chats_repo = repositories.ChatsRepo()
    return chats_repo

@pytest.fixture(scope='function')
def chat_repo():
    chat_repo = repositories.ChatRepo()
    return chat_repo

@pytest.fixture(scope='function')
def service_user(users_repo):
    return services.Users(users_repo=users_repo)

@pytest.fixture(scope='function')
def service_chats(chats_repo):
    return services.Chats(chats_repo=chats_repo)

@pytest.fixture
def for_delete(service_chats, service_user):
    user1 = services.UserInfo(name="Dima", password="123")
    service_user.create_user(user1)
    chat = services.ChatInfo(
        title="First",
        description="FFF",
    )
    user = services.User_initiator(id=0)
    service_chats.create_chat(chat, user)

@pytest.fixture(scope='function')
def service_chat(chat_repo):
    return services.Chat(chat_repo=chat_repo)

@pytest.fixture(scope='function')
def filin_db(service_chats, service_user, service_chat):
    user1 = services.UserInfo(name="Dima", password="123")
    user2 = services.UserInfo(name="Dmitry", password="123")
    service_user.create_user(user1)
    service_user.create_user(user2)
    chat = services.ChatInfo(
        title="First",
        description="FFF",
    )
    user = services.User_initiator(id=0)
    service_chats.create_chat(chat, user)
    chat_in = services.ChatActionInfo(chat_id=0)