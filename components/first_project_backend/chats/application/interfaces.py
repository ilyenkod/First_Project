from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import User


class UsersRepo(ABC):

    @abstractmethod
    def create_user(self, name: str):
        pass


class ChatRepo(ABC):

    @abstractmethod
    def get_information(self, chat_id: int, user_init_id: int):
        pass

    @abstractmethod
    def get_users(self, user_init_id: int, chat_id: int):
        pass

    @abstractmethod
    def send_message(self, user: int, message: str, chat_id: int):
        pass

    @abstractmethod
    def get_messages(self, user_init: User):
        pass

    @abstractmethod
    def leave_chat(self, chat_id: int, user_id: int):
        pass

    @abstractmethod
    def is_participant(self, user_id: int, chat_id: int):
        pass


    # @abstractmethod
    # def delete_user(self, user_init_id: int, user_id: int, chat_id: int):
    #     pass


class ChatsRepo(ABC):

    @abstractmethod
    def create_chat(self, id: int, user_owner_id: int, title: str, description: str):
        pass

    @abstractmethod
    def delete_chat(self, user_init_id: int, id_chat: int):
        pass

    @abstractmethod
    def get_len(self):
        pass

    @abstractmethod
    def update_information(self, chat_id: int, user_init: int, title: Optional[str] = None,
                           description: Optional[str] = None):
        pass

    @abstractmethod
    def add_user(self, user_init_id: int, user_id: int, chat_id: int):
        pass

    @abstractmethod
    def is_owner(self, user_init_id: id, id_chat: int):
        pass