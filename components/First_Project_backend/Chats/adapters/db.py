from classic.components import component


class User:
    def __init__(self, user_id: int, name: str, chats: list):
        self.user_id = user_id
        self.name = name
        self.chats = [
            {
                chat_id: None,
                user_or_admin: False
            }
        ]

    # user_id: int
    # name: str
    # chats: list


class Chat:
    def __init__(self, chat_id: int, creator_id: int, users_list: list, users_left: list):
        self.chat_id = chat_id
        self.creator_id = creator_id
        self.users_list = users_list
        self.users_left = users_left
        self.messages = list()

