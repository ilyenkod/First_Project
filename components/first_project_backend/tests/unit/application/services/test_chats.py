import pytest

from components.first_project_backend.chats.adapters.database.tables import chats_base
from components.first_project_backend.chats.application import services


def test_create_chat(service_user, service_chats):
    user1 = services.UserInfo(name="Dima", password="123")
    service_user.create_user(user1)
    chat = services.ChatInfo(
    title="First",
    description="FFF",
    )
    user = services.User_initiator(id=0)
    firt_len = len(chats_base)
    service_chats.create_chat(chat, user)
    second_len = len(chats_base)
    assert second_len == firt_len + 1

def test_add_user(service_chat, filin_db, service_chats):
    user_init = services.User_initiator(id=0)
    user_add = services.ChatAddUser(user_id=1, chat_id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    first = service_chat.get_users(chat_in, user_init)
    service_chats.add_user(user_add, user_init)
    second = service_chat.get_users(chat_in, user_init)
    assert len(first.users) + 1 == len(second.users)

def test_put_information(service_chat, filin_db, service_chats):
    user = services.User_initiator(id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    chat_update = services.ChatUpdate(
        chat_id=0,
        title="Changed",
        description="Changed"
    )
    service_chats.update_information(chat_update, user)
    information = service_chat.get_information(chat_in, user)
    assert information.title == chat_update.title and information.description == chat_update.description

def test_delete_chat(service_user, service_chats, for_delete):
    user = services.User_initiator(id=0)
    del_chat = services.ChatActionInfo(
        chat_id=0
    )
    firt_len = len(chats_base)
    service_chats.delete_chat(del_chat, user)
    second_len = len(chats_base)
    assert second_len == firt_len - 1




