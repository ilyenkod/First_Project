import falcon

from components.first_project_backend.chats.adapters.chat_api import controllers
from components.first_project_backend.chats.adapters.chat_api.auth import AddHeaderComponent, Middleware
from components.first_project_backend.chats.application import services


def create_app( users: services.Users, chat: services.Chat, chats: services.Chats):

    middlewares = [
        AddHeaderComponent(),
        Middleware()
    ]

    app = falcon.App(middleware=middlewares)

    app.add_route('/chats/', controllers.Chats(chats=chats, chat=chat))
    app.add_route('/login/', controllers.AddUser(users=users))
    app.add_route('/users/', controllers.ChatUsers(chat=chat))
    app.add_route('/messages/', controllers.Message(chat=chat))

    return app

