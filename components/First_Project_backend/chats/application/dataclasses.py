import datetime
from typing import List, Optional

import attr


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


@attr.dataclass
class Message:
    author: str
    text: str
    date: datetime.datetime
