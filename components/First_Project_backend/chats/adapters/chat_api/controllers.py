import base64
import hashlib
import json
import falcon

from classic.components import component
from wsgiref.simple_server import make_server

from components.First_Project_backend.chats.application import services
from components.First_Project_backend.chats.adapters.database.tables import chats_base, users_base

def return_user_id(auth_hashed_data: str, login=True):
    auth_hashed_data = auth_hashed_data.split()[1]
    auth_data = base64.b64decode(auth_hashed_data).decode('utf-8')
    auth_data = auth_data.split(':')
    if login:
        for_return = {
            "id": auth_data[0]
        }
        return services.User_initiator.parse_obj(for_return)
    else:
        for_return = {
            "name": auth_data[0],
            "password": auth_data[1]
        }
        return services.UserInfo.parse_obj(for_return)




@component
class AddUser:

    users: services.Users
    # def __init__(self, users: services.Users):
    #     self.users = users

    #Добавить пользователя
    def on_post(self, req, resp):
        try:
            new_user = req.get_media()
            user_info = services.UserInfo.parse_obj(new_user)
            #new_user = return_user_id(req.headers.get('AUTHORIZATION'), login=False)
            self.users.create_user(user_info)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Сan't add a user")
        resp.status = falcon.HTTP_201

@component
class Chats:

    chats: services.Chats
    chat: services.Chat

    # def __init__(self, chats: services.Chats, chat: services.Chat):
    #     self.chats = chats
    #     self.chat = chat

    #Удалить чат
    def on_delete(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            info = req.get_media()
            chat_delete_info = services.ChatActionInfo.parse_obj(info)
            self.chats.delete_chat(chat_delete_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't delete chat")
        resp.status = falcon.HTTP_204

    #Создать чат
    def on_post(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            new_chat = req.get_media()
            chat_info = services.ChatInfo.parse_obj(new_chat)
            self.chats.create_chat(chat_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't create a chat")

        resp.status = falcon.HTTP_201

    #Получить информацию о чате
    def on_get(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            info = req.get_media()
            chat_init_info = services.ChatActionInfo.parse_obj(info)
            chat_information = self.chat.get_information(chat_init_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't get chat information")
        for_return = {"title": chat_information.title, "description": chat_information.description}
        resp.body = json.dumps(for_return)
        resp.status = falcon.HTTP_200

    #Обновить информацию о чате
    def on_put(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            update = req.get_media()
            chat_update = services.ChatUpdate.parse_obj(update)
            self.chat.update_information(chat_update, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't put chat information")
        resp.status = falcon.HTTP_204

@component
class ChatUsers:

    chat: services.Chat
    # def __init__(self, chat: services.Chat):
    #     self.chat = chat

    #Добавить пользователя в чат
    def on_post(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            new_chat = req.get_media()
            user_info = services.ChatAddUser.parse_obj(new_chat)
            self.chat.add_user(user_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't add in chat")
        resp.status = falcon.HTTP_201

    #Пользователю уйти
    def on_delete(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            info = req.get_media()
            chat_delete_info = services.ChatActionInfo.parse_obj(info)
            self.chat.leave_chat(chat_delete_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't leave chat")
        resp.status = falcon.HTTP_204

    #Получить список пользователей чата
    def on_get(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            info = req.get_media()
            users_init_info = services.ChatActionInfo.parse_obj(info)
            users_information = self.chat.get_users(users_init_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't get list of users")
        for_return = {"users": users_information.users}
        resp.body = json.dumps(for_return)
        resp.status = falcon.HTTP_200

@component
class Message:
    chat: services.Chat
    # def __init__(self, chat: services.Chat):
    #     self.chat = chat

    #Отправить сообщение
    def on_post(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            new_messsage = req.get_media()
            message_info = services.MessageInfo.parse_obj(new_messsage)
            self.chat.send_message(message_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't add in chat")
        resp.status = falcon.HTTP_201

    #Получить список сообщений чата
    def on_get(self, req, resp):
        try:
            user_id = return_user_id(req.headers.get('AUTHORIZATION'))
            info = req.get_media()
            message_info = services.ChatActionInfo.parse_obj(info)
            message_information = self.chat.get_messages(message_info, user_id)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't get list of users")
        for_return = {"messages": message_information.messages}
        resp.body = json.dumps(for_return)
        resp.status = falcon.HTTP_200


