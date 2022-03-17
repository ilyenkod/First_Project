from classic.components import component
import datetime
from typing import Optional

from components.First_Project_backend.chats.application import interfaces
from components.First_Project_backend.chats.application.dataclasses import User, Chat, Message
from tables import users, chats


class UsersRepo(interfaces.UsersRepo):

    def create_user(self, name: str):
        n = len(users)
        new_user = User(n, name)
        users.append(new_user)

    def get_by_id(self, id: int) -> User:
        return users[id-1]

class ChatsRepo(interfaces.ChatsRepo):

    def create_chat(self, user_owner: User, title: str, description: str):
        n = len(chats)
        new_chat = Chat(n, user_owner.user_id, title, description)
        chats.append(new_chat)

    def delete_chat(self, user_init: User, id_chat: int):
        if chats[id_chat-1].creator_id == user_init.id:
            del chats[id_chat-1]
        else:
            raise Exception("Нет прав для удаления")

    def get_chat(self, id_chat: int) -> Chat:
        return chats[id_chat-1]

@component()
class ChatRepo(interfaces.ChatRepo):
    my_chat: Chat

    def update_information(self, user_init: User, title: Optional[str] = None, description: Optional[str] = None):
        if user_init.id != self.my_chat.creator_id:
            raise Exception("Пользователь не может редактировать чат")
        else:
            if title is not None:
                self.my_chat.title = title
            if description is not None:
                self.my_chat.description = description


    def get_information(self, user_init: User):
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


    def send_message(self, user_init: User, message: str):
        if user_init not in self.my_chat.users_list:
            raise Exception("Пользователь не может отправить сообщение")
        else:
            my_message = Message(user_init.name, message, datetime.datetime.now())
            self.my_chat.messages.append(my_message)



    def get_messages(self, user_init: User):
        if user_init not in self.my_chat.users_list:
            raise Exception("Пользователь не может получить список сообщений")
        else:
            return self.my_chat.return_messages_list()

