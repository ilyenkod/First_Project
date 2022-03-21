import pytest

from components.first_project_backend.chats.application import services


def test_get_information(service_chat, filin_db):
    user = services.User_initiator(id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    information = service_chat.get_information(chat_in, user)
    assert isinstance(information, services.ChatInfo)


def test_get_users(service_chat, filin_db):
    user = services.User_initiator(id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    information = service_chat.get_users(chat_in, user)
    assert isinstance(information, services.UsersList)


def test_leave_chat(service_chat, filin_db, service_chats):
    user_init = services.User_initiator(id=0)
    user_add = services.ChatAddUser(user_id=1, chat_id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    service_chats.add_user(user_add, user_init)
    first = service_chat.get_users(chat_in, user_init)
    user_leave = services.User_initiator(id=1)
    service_chat.leave_chat(chat_in, user_leave)
    second = service_chat.get_users(chat_in, user_init)
    assert len(first.users) - 1 == len(second.users)

def test_get_messages(service_chat, filin_db):
    user_init = services.User_initiator(id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    information = service_chat.get_messages(chat_in, user_init)
    assert isinstance(information, services.MessageList)

def test_send_message(service_chat, filin_db):
    user_init = services.User_initiator(id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    message = services.MessageInfo(
        text="First_message",
        chat_id="0"
    )
    first = service_chat.get_messages(chat_in, user_init)
    service_chat.send_message(message, user_init)
    second = service_chat.get_messages(chat_in, user_init)
    assert len(first.messages) + 1 == len(second.messages)


def test_leave_and_delete(service_chat, filin_db, service_chats):
    user_init = services.User_initiator(id=0)
    user_add = services.ChatAddUser(user_id=1, chat_id=0)
    chat_in = services.ChatActionInfo(chat_id=0)
    service_chats.add_user(user_add, user_init)
    user_leave = services.User_initiator(id=0)
    service_chat.leave_chat(chat_in, user_leave)
    with pytest.raises(Exception):
        second = service_chat.get_users(chat_in, user_init)


