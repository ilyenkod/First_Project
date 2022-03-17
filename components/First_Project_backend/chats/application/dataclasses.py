import attr
import datetime
from typing import List, Optional


@attr.dataclass
class User:
    id: int
    name: str


@attr.dataclass
class Chat:

    id: int
    creator_id: int
    title: str
    description: str
    users_list : Optional[List]
    users_left : Optional[List]
    messages : Optional[List]

    def return_messages_list(self):
        messages_list = []
        for mes in self.messages:
            messages_list.append((mes.name, mes.text, mes.date))
        return messages_list


@attr.dataclass
class Message:
    name: str
    text: str
    date: datetime.datetime
