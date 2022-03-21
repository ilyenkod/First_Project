from unittest.mock import Mock

from components.first_project_backend.chats.adapters.database.tables import chats_base
from components.first_project_backend.chats.application import services



def test_create_chat(service_chats):
    chat = services.ChatInfo(
    title="First",
    description="FFF",
    )
    user = services.User_initiator(id=0)
    service_chats.create_chat(chat, user)
    service_chats.chats_repo.create_chat.assert_called_once()

def test_delete_user(service_chats):
    service_chats.chat_repo.in_leave_list.return_value = False
    user_init = services.User_initiator(id=0)
    user_add = services.ChatAddUser(user_id=1, chat_id=0)
    service_chats.delete_user(user_add, user_init)
    service_chats.chats_repo.delete_user.assert_called_once()

def test_add_user(service_chats):
    service_chats.chat_repo.is_participant.return_value = False
    service_chats.chat_repo.in_leave_list.return_value = False
    user_init = services.User_initiator(id=0)
    user_add = services.ChatAddUser(user_id=1, chat_id=0)
    service_chats.add_user(user_add, user_init)
    service_chats.chats_repo.add_user.assert_called_once()



def test_put_information(service_chats):
    user = services.User_initiator(id=0)
    chat_update = services.ChatUpdate(
        chat_id=0,
        title="Changed",
        description="Changed"
    )
    service_chats.update_information(chat_update, user)
    service_chats.chats_repo.update_information.assert_called_once()


def test_delete_chat(service_chats, service_chat):
    user = services.User_initiator(id=0)
    del_chat = services.ChatActionInfo(
        chat_id=0
    )
    service_chats.delete_chat(del_chat, user)
    service_chats.chats_repo.delete_chat.assert_called_once()




