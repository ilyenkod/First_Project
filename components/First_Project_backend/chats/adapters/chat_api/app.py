import falcon

from components.First_Project_backend.chats.application import services
from components.First_Project_backend.chats.adapters.chat_api import controllers
from components.First_Project_backend.chats.adapters.chat_api.auth import AddHeaderComponent, Middleware


def create_app( users: services.Users, chat: services.Chat, chats: services.Chats):

    middlewares = [
        AddHeaderComponent(),
        Middleware()
    ]

    app = falcon.App(middleware=middlewares)

    app.add_route('/chats/', controllers.Chats(chats, chat))
    app.add_route('/login/', controllers.AddUser(users))
    app.add_route('/users/', controllers.ChatUsers(chat))
    app.add_route('/messages/', controllers.Message(chat))

    return app

