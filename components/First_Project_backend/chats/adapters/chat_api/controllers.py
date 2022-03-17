from classic.components import component
import falcon
import json
from wsgiref.simple_server import make_server
from pydantic import BaseModel

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


class Chats:

    def __init__(self, chats: services.Chats):
        self.chats = chats

    def on_get_header(self, req, resp, chat_id):
        if int(chat_id) > self.chats.get_len() - 1:
            raise MyException.handle(req, resp, "Not id", "Params")
        resp.text = json.dumps(self.chats.get_chat_by_id(int(chat_id)))
        resp.status = falcon.HTTP_200

class SendMessage:

    def __init__(self, chat: services.Chat):
        self.chat = chat

    def on_post(self, req, resp):
        mess = req.get_media()
        self.chat.send_message(mess["Message"], mess["Author"])
        resp.status = falcon.HTTP_201






