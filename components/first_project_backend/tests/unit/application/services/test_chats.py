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

def test_delete_chat(service_user, service_chats, for_delete):
    user = services.User_initiator(id=0)
    del_chat = services.ChatActionInfo(
        chat_id=0
    )
    firt_len = len(chats_base)
    service_chats.delete_chat(del_chat, user)
    second_len = len(chats_base)
    assert second_len == firt_len - 1


