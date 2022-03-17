from abc import ABC, abstractmethod
from .dataclasses import User, Chat

class UsersRepo(ABC):

    @abstractmethod
    def create_user(self, id: int, name: str) -> User:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> User:
        pass

class ChatRepo(ABC):

    @abstractmethod
    def create_chat(self, user_owner: User, id_chat: int) -> Chat:
        pass

    @abstractmethod
    def update_information(self):
        pass

    @abstractmethod
    def delete_chat(self, user_init: User, id_chat: int):
        pass

    @abstractmethod
    def get_information(self, user_init: User, id_chat: int):
        pass

    @abstractmethod
    def add_user(self, user_init: User, user: User, id_chat: int):
        pass