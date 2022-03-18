from classic.components import component
import datetime
from typing import Optional

from components.First_Project_backend.chats.application import interfaces
from components.First_Project_backend.chats.application.dataclasses import User, Chat, Message
from components.First_Project_backend.chats.adapters.database.tables import chats_base, users_base, users_log

def get_user_by_id(in_id: int):
    for user in users_base:
        if user.id == in_id:
            return user
    raise Exception("Пользователя с таким id не существует")

def get_chat_by_id(in_id: int):
    for chat in chats_base:
        if chat.id == in_id:
            return chat
    raise Exception("Чата с таким id не существует")


class UsersRepo(interfaces.UsersRepo):

    def create_user(self, name: str, password: str):
        n = len(users_base)
        new_user = User(n, name)
        for_auth = {
            "login": str(n),
            "password": password
        }
        users_base.append(new_user)
        users_log.append(for_auth)


class ChatsRepo(interfaces.ChatsRepo):

    def create_chat(self, user_owner_id: int, title: str, description: str):
        if get_user_by_id(user_owner_id):
            n = len(chats_base)
            new_chat = Chat(id=n, creator_id=user_owner_id, title=title, description=description,
                            users_list=list(), users_left=list(), messages=list())
            new_chat.users_list.append(get_user_by_id(user_owner_id))
            chats_base.append(new_chat)

    def delete_chat(self, user_init_id: id, id_chat: int):
        now_chat = get_chat_by_id(id_chat)
        if now_chat.creator_id == user_init_id:
            number_in_base = chats_base.index(get_chat_by_id(id_chat))
            del chats_base[number_in_base]
        else:
            raise Exception("Нет прав для удаления")


    def get_len(self):
        return len(chats_base)


class ChatRepo(interfaces.ChatRepo):

    #my_chat: Chat

    # def __init__(self, my_chat: Chat):
    #     self.my_chat = my_chat

    def update_information(self, chat_id: int, user_init: int, title: Optional[str] = None,
                           description: Optional[str] = None):
        my_chat = get_chat_by_id(chat_id)
        if user_init != my_chat.creator_id:
            raise Exception("Пользователь не может редактировать чат")
        else:
            if title is not None:
                my_chat.title = title
            if description is not None:
                my_chat.description = description


    def get_information(self, chat_id: int, user_init_id: id):
        my_chat = get_chat_by_id(chat_id)
        my_user = get_user_by_id(user_init_id)
        if my_user not in my_chat.users_list:
            raise Exception("Пользователь не может получить информацию о чате")
        else:
            for_return = {'creator_id': my_chat.creator_id, 'title': my_chat.title,
                          'description': my_chat.description}
            return  for_return


    def add_user(self, user_init_id: int, user_id: int, chat_id: int):
        my_chat = get_chat_by_id(chat_id)
        my_user = get_user_by_id(user_id)
        if user_init_id != my_chat.creator_id:
            raise Exception("Пользователь не может добавить в чат другого пользователя")
        else:
            my_chat.users_list.append(my_user)


    def get_users(self, user_init_id: int, chat_id: int):
        my_chat = get_chat_by_id(chat_id)
        my_user = get_user_by_id(user_init_id)
        if my_user not in my_chat.users_list:
            raise Exception("Пользователь не может получить список участников чата")
        else:
            users_list = {
                "users": []
            }
            for i in my_chat.users_list:
                users_list["users"].append(i.name)
            return users_list


    def send_message(self, user: int, message: str, chat_id: int):
        my_user = get_user_by_id(user)
        my_chat = get_chat_by_id(chat_id)
        my_message = Message(my_user.name, message, datetime.datetime.now())
        my_chat.messages.append(my_message)



    def get_messages(self, user_init: User):
        if user_init not in self.my_chat.users_list:
            raise Exception("Пользователь не может получить список сообщений")
        else:
            return self.my_chat.return_messages_list()

    def leave_chat(self, chat_id: int, user_id: int):
        my_chat = get_chat_by_id(chat_id)
        my_user = get_user_by_id(user_id)
        if my_user not in my_chat.users_list:
            raise Exception("Пользователь не состоит в чате")
        elif my_user.id == my_chat.creator_id:
            chats_base.remove(my_chat)
        else:
            my_chat.users_list.remove(my_user)
            my_chat.users_left.append(my_user)

