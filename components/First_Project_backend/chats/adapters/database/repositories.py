from classic.components import component
import datetime
from typing import Optional

from components.First_Project_backend.chats.application import interfaces
from components.First_Project_backend.chats.application.dataclasses import User, Chat, Message
from components.First_Project_backend.chats.adapters.database.tables import chats_base, users_base

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

    def create_user(self, name: str):
        n = len(users_base)
        new_user = User(n, name)
        users_base.append(new_user)

    def get_by_id(self, id: int) -> User:
        return users_base[id]

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

    def get_chat(self, id_chat: int) -> Chat:
        return chats_base[id_chat]

    def get_len(self):
        return len(chats_base)


class ChatRepo(interfaces.ChatRepo):

    #my_chat: Chat

    # def __init__(self, my_chat: Chat):
    #     self.my_chat = my_chat

    def update_information(self, chat_id: int, user_init: User, title: Optional[str] = None,
                           description: Optional[str] = None):
        if user_init.id != self.my_chat.creator_id:
            raise Exception("Пользователь не может редактировать чат")
        else:
            if title is not None:
                self.my_chat.title = title
            if description is not None:
                self.my_chat.description = description


    def get_information(self, chat_id: int, user_init: User):
        my_chat = chats_base[chat_id]
        if user_init not in self.my_chat.users_list:
            raise Exception("Пользователь не может получить информацию о чате")
        else:
            return self.my_chat.title, self.my_chat.description


    def add_user(self, user_init: User, user: User):
        if user_init.id != self.my_chat.creator_id:
            raise Exception("Пользователь не может добавить в чат другого пользователя")
        else:
            self.my_chat.users_list.append(user)


    def get_users(self, user_init: User):
        if user_init not in self.my_chat.users_list:
            raise Exception("Пользователь не может получить список участников чата")
        else:
            users_list = []
            for i in self.my_chat.users_list:
                users_list.append(i.name)
            return users_list


    def send_message(self, mess):
        # if user_init not in self.my_chat.users_list:
        #     raise Exception("Пользователь не может отправить сообщение")
        # else:
        print(mess.author)
        my_message = Message(mess.author, mess.text, datetime.datetime.now())
        self.my_chat.messages.append(my_message)



    def get_messages(self, user_init: User):
        if user_init not in self.my_chat.users_list:
            raise Exception("Пользователь не может получить список сообщений")
        else:
            return self.my_chat.return_messages_list()

