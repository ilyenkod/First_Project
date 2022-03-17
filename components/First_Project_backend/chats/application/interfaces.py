from abc import ABC, abstractmethod
from .dataclasses import User, Chat
from typing import Optional

class UsersRepo(ABC):

    @abstractmethod
    def create_user(self, name: str):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> User:
        pass


class ChatRepo(ABC):

    @abstractmethod
    def update_information(self, user_init: User, title: Optional[str] = None, description: Optional[str] = None):
        pass

    @abstractmethod
    def get_information(self, user_init: User):
        pass

    @abstractmethod
    def add_user(self, user_init: User, user: User):
        pass

    @abstractmethod
    def get_users(self, user_init: User):
        pass

    @abstractmethod
    def send_message(self, user_init: User, message: str):
        pass

    @abstractmethod
    def get_messages(self, user_init: User):
        pass



class ChatsRepo(ABC):

    @abstractmethod
    def create_chat(self, id: int, user_owner: User, title: str, description: str):
        pass

    @abstractmethod
    def delete_chat(self, user_init: User, id_chat: int):
        pass

    @abstractmethod
    def get_chat(self, id_chat: int) -> Chat:
        pass