from classic.components import component


@component
class User:
    user_id: int
    name: str


@component
class Chat:
    chat_id = int()
    creator_id = int()
    users_list = list()
    users_left = list()
    messages = list()

