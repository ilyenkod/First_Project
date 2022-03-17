import attr
import datetime

@attr.dataclass
class User:
    user_id: int
    name: str


@attr.dataclass
class Chat:
    chat_id = int
    creator_id = int
    title: str
    description: str
    users_list = list
    users_left = list
    messages = list

@attr.dataclass
class message:
    author_id: int
    text: str
    date: datetime.datetime
