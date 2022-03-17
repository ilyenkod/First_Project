import attr

@attr.dataclass
class User:
    user_id: int
    name: str


@attr.dataclass
class Chat:
    chat_id = int
    creator_id = int
    users_list = list
    users_left = list
    messages = list

