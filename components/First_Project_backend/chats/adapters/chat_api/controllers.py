from classic.components import component
import falcon
import json
from wsgiref.simple_server import make_server

from components.First_Project_backend.chats.application import services
from components.First_Project_backend.chats.adapters.database.tables import chats_base, users_base

class MyException(BaseException):
    @staticmethod
    def handle(req, resp, exc, params):
        resp.set_header("X-Custom-Header", "id not found")
        # resp.body = json.dumps({"field": "value"})
        raise falcon.HTTPBadRequest(
            "id not found",
            "You need choose another id"
        )



class SendMessage:

    def __init__(self, chat: services.Chat):
        self.chat = chat

    def on_post(self, req, resp):
        mess = req.get_media()
        message = services.MessageInfo.parse_obj(mess)
        self.chat.send_message(message)
        resp.status = falcon.HTTP_201

class AddUser:

    def __init__(self, users: services.Users):
        self.users = users

    def on_post(self, req, resp):
        try:
            new_user = req.get_media()
            user_info = services.UserInfo.parse_obj(new_user)
            self.users.create_user(user_info)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Сan't add a user")
        resp.status = falcon.HTTP_201

class Chats:

    def __init__(self, chats: services.Chats, chat: services.Chat):
        self.chats = chats
        self.chat = chat

    def on_delete(self, req, resp):
        try:
            info = req.get_media()
            chat_delete_info = services.ChatActionInfo.parse_obj(info)
            self.chats.delete_chat(chat_delete_info)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't delete chat")
        resp.status = falcon.HTTP_204

    def on_post(self, req, resp):
        try:
            new_chat = req.get_media()
            chat_info = services.ChatInfo.parse_obj(new_chat)
            self.chats.create_chat(chat_info)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't add a chat")
        resp.status = falcon.HTTP_201


    def on_get(self, req, resp):
        try:
            info = req.get_media()
            chat_init_info = services.ChatActionInfo.parse_obj(info)
            chat_information = self.chat.get_information(chat_init_info)
        except Exception as e:
            raise falcon.HTTPNotFound(title="Can't get chat information")
        for_return = {"title": chat_information.title, "description": chat_information.description}
        resp.body = json.dumps(for_return)
        resp.status = falcon.HTTP_200







