from classic.http_api import App

from components.first_project_backend.chats.adapters.chat_api import controllers
from components.first_project_backend.chats.adapters.chat_api.auth import AddHeaderComponent, Middleware
from components.first_project_backend.chats.application import services


def create_app( users: services.Users, chat: services.Chat, chats: services.Chats):

    middlewares = [
        AddHeaderComponent(),
        Middleware()
    ]

    app = App(middleware=middlewares, prefix='/api')
    app.register(controllers.AddUser(users=users), url='/user')
    app.register(controllers.Chats(chats=chats, chat=chat))
    app.register(controllers.ChatUsers(chat=chat), url='/chat')
    app.register(controllers.Message(chat=chat))

    return app

