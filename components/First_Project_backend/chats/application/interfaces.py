from abc import ABC, abstractmethod
from .dataclasses import User, Chat


class UsersRepo(ABC):

    @abstractmethod
    def create_user(self, name: str):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> User:
        pass


class ChatRepo(ABC):

    @abstractmethod
    def update_information(self):
        pass

    @abstractmethod
    def get_information(self, user_init: User):
        pass

    @abstractmethod
    def add_user(self, user_init: User, user: User):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def send_message(self, user_init: User, message: str):
        pass

    @abstractmethod
    def get_message(self):
        pass



class ChatsRepo(ABC):

    @abstractmethod
    def create_chat(self, user_owner: User):
        pass

    @abstractmethod
    def delete_chat(self, user_init: User, id_chat: int):
        pass

    @abstractmethod
    def get_chat(self, id_chat: int) -> Chat:
        pass