from classic.components import component
from typing import Optional


from components.First_Project_backend.chats.application.dataclasses import User, Chat, Message

from components.First_Project_backend.chats.application import interfaces
from components.First_Project_backend.chats.adapters.database.repositories import UsersRepo, ChatRepo, ChatsRepo
from components.First_Project_backend.chats.adapters.database.tables import chats_base, users_base



class Users:

    # users_repo: interfaces.UsersRepo
    def __init__(self, users_repo: interfaces.UsersRepo):
        self.users_repo = users_repo


    def create_user(self, name: str):
        self.users_repo.create_user(name)

    def get_user_by_id(self, id: int):
        return self.users_repo.get_by_id(id)


class Chats:

    #chats_repo: interfaces.ChatsRepo
    def __init__(self, chats_repo: interfaces.ChatsRepo):
        self.chats_repo = chats_repo

    def create_chat(self, user_owner: User, title: str, description: str):
        self.chats_repo.create_chat(user_owner, title, description)

    def delete_chat(self, user_init: User, id_chat: int):
        self.chats_repo.delete_chat(user_init, id_chat)

    def get_chat_by_id(self, id_chat: int) -> Chat:
        return self.chats_repo.get_chat(id_chat)

    def get_len(self):
        return self.chats_repo.get_len()


class Chat:

    #chat_repo: interfaces.ChatRepo
    def __init__(self, chat_repo: interfaces.ChatRepo):
        self.chat_repo = chat_repo

    def update_information(self, user_init: User, title: Optional[str] = None, description: Optional[str] = None):
        self.chat_repo.update_information(user_init, title, description)

    def get_information(self, user_init: User):
        return self.chat_repo.get_information(user_init)

    def add_user(self, user_init: User, user: User):
        self.chat_repo.add_user(user_init, user)

    def get_users(self, user_init: User):
        self.chat_repo.get_users(user_init)

    def send_message(self, user_name: str, message: str):
        self.chat_repo.send_message(user_name, message)

    def get_messages(self, user_init: User):
        return self.chat_repo.get_messages(user_init)


# my_prom_users = UsersRepo()
#
# my_prom_chats = ChatsRepo()
#
#
# my_users = Users(my_prom_users)
# my_chats = Chats(my_prom_chats)
#
# my_users.create_user("Дима")
#
#
# my_chats.create_chat(my_users.get_user_by_id(0), "First_chat", "FFF")
# #print(my_chats.get_chat_by_id(0))
# prom_chat = ChatRepo(my_chats.get_chat_by_id(0))
# print(my_chats.get_chat_by_id(0).users_list)
# my_chat = Chat(prom_chat)
#
# my_chat.send_message(my_users.get_user_by_id(0), "First message")
#
# print(my_chats.get_chat_by_id(0))
#
# print(my_chat.get_information(my_users.get_user_by_id(0)))

# my_chats.delete_chat(my_users.get_user_by_id(0), 0)
# print(my_chats)