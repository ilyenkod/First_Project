from classic.components import component
from typing import Optional
from classic.app import DTO, validate_with_dto

from components.First_Project_backend.chats.application.dataclasses import User, Chat, Message

from components.First_Project_backend.chats.application import interfaces
from components.First_Project_backend.chats.adapters.database.repositories import UsersRepo, ChatRepo, ChatsRepo
from components.First_Project_backend.chats.adapters.database.tables import chats_base, users_base

class MessageInfo(DTO):
    author: int
    text: str
    chat_id: int

class UserInfo(DTO):
    name: str
    password: str

class ChatInfo(DTO):
    creator_id: int
    title: str
    description: str

class ChatActionInfo(DTO):
    initiator_id: int
    chat_id: int

class ChatUpdate(DTO):
    initiator_id: int
    chat_id: int
    title: str
    description: str

class ChatAddUser(DTO):
    init_id: int
    user_id: int
    chat_id: int

class UsersList(DTO):
    users: list

class MessageList(DTO):
    messages: list


class Users:

    # users_repo: interfaces.UsersRepo
    def __init__(self, users_repo: interfaces.UsersRepo):
        self.users_repo = users_repo

    def create_user(self, user_info: UserInfo):
        self.users_repo.create_user(user_info.name, user_info.password)



class Chats:

    #chats_repo: interfaces.ChatsRepo
    def __init__(self, chats_repo: interfaces.ChatsRepo):
        self.chats_repo = chats_repo

    def create_chat(self, chat_info: ChatInfo):
        self.chats_repo.create_chat(chat_info.creator_id, chat_info.title, chat_info.description)

    def delete_chat(self, chat_delete_info: ChatActionInfo):
        self.chats_repo.delete_chat(chat_delete_info.initiator_id, chat_delete_info.chat_id)

    def get_len(self):
        return self.chats_repo.get_len()


class Chat:

    #chat_repo: interfaces.ChatRepo
    def __init__(self, chat_repo: interfaces.ChatRepo):
        self.chat_repo = chat_repo

    def update_information(self, chat_update: ChatUpdate):
        self.chat_repo.update_information(chat_update.initiator_id, chat_update.chat_id,
                                          chat_update.title, chat_update.description)

    def get_information(self, chat_init_info: ChatActionInfo):
        information = self.chat_repo.get_information(chat_init_info.chat_id, chat_init_info.initiator_id)
        for_return = ChatInfo.parse_obj(information)
        return for_return

    def add_user(self, information: ChatAddUser):
        self.chat_repo.add_user(information.init_id, information.user_id, information.chat_id)

    def get_users(self, user_init: ChatActionInfo):
        information = self.chat_repo.get_users(user_init.initiator_id, user_init.chat_id)
        for_return = UsersList.parse_obj(information)
        return for_return

    def send_message(self, message: MessageInfo):
        self.chat_repo.send_message(message.author, message.text, message.chat_id)

    def get_messages(self, message_info: ChatActionInfo):
        information = self.chat_repo.get_messages(message_info.initiator_id, message_info.chat_id)
        print(type(information))
        print(information)
        for_return = MessageList.parse_obj(information)
        return for_return

    def leave_chat(self, chat_action: ChatActionInfo):
        self.chat_repo.leave_chat(chat_action.chat_id, chat_action.initiator_id)
