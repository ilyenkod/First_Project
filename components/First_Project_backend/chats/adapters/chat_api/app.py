import falcon
from wsgiref.simple_server import make_server

from components.First_Project_backend.chats.application import services
from components.First_Project_backend.chats.adapters.database.repositories import ChatsRepo, ChatRepo, UsersRepo
from components.First_Project_backend.chats.adapters.chat_api import controllers
from components.First_Project_backend.chats.adapters.chat_api.auth import AddHeaderComponent, Middleware

#app = falcon.App()

middlewares = [
    AddHeaderComponent(),
    Middleware()
]

app = falcon.App(middleware=middlewares)

my_prom_chats = ChatsRepo()
my_prom2_chats = services.Chats(my_prom_chats)

my_prom_chat = ChatRepo()
my_prom2_chat = services.Chat(my_prom_chat)
my_chats= controllers.Chats(my_prom2_chats, my_prom2_chat)


user_chat = controllers.ChatUsers(my_prom2_chat)



my_prom_users = UsersRepo()
my_prom2_users = services.Users(my_prom_users)
my_user = controllers.AddUser(my_prom2_users)


app.add_route('/chats/', my_chats)
app.add_route('/login/', my_user)
app.add_route('/users/', user_chat)

with make_server('localhost', 8000, app) as httpd:
    print(f"server starting on http://localhost:{httpd.server_port}")
    httpd.serve_forever()
