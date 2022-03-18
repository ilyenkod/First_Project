import pytest

from components.First_Project_backend.chats.adapters.database.tables import chats_base
from components.First_Project_backend.chats.application import services

@pytest.fixture(scope='function')
def service(users_repo):
    return services.Users(users_repo=users_repo)

@pytest.fixture(scope='function')
def service1(chats_repo):
    return services.Chats(chats_repo=chats_repo)



def test_create_chat(service1, service):
    user1 = services.UserInfo(name="Dima", password="123")
    service.create_user(user1)
    chat = services.ChatInfo(
    title="First",
    description="FFF",
    )
    user = services.User_initiator(id=0)
    firt_len = len(chats_base)
    service1.create_chat(chat, user)
    second_len = len(chats_base)
    assert second_len == firt_len + 1

def test_delete_chat(service1, service):
    user1 = services.UserInfo(name="Dima", password="123")
    service.create_user(user1)
    chat = services.ChatInfo(
        title="First",
        description="FFF",
    )
    user = services.User_initiator(id=0)
    service1.create_chat(chat, user)
    del_chat = services.ChatActionInfo(
        chat_id=0
    )
    firt_len = len(chats_base)
    service1.delete_chat(del_chat, user)
    second_len = len(chats_base)
    assert second_len == firt_len - 1


