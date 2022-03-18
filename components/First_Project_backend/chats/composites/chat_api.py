from wsgiref.simple_server import make_server
from components.First_Project_backend.chats.adapters.chat_api import app
from components.First_Project_backend.chats.adapters import database
from components.First_Project_backend.chats.application import services

class DB:
    user_repo = database.repositories.UsersRepo()
    chat_repo = database.repositories.ChatRepo()
    chats_repo = database.repositories.ChatsRepo()

class Application:

    users = services.Users(users_repo=DB.user_repo)
    chat = services.Chat(chat_repo=DB.chat_repo)
    chats = services.Chats(chats_repo=DB.chats_repo)


app = app.create_app(users=Application.users, chat=Application.chat, chats=Application.chats)


with make_server('localhost', 8000, app) as httpd:
    print(f"server starting on http://localhost:{httpd.server_port}")
    httpd.serve_forever()



