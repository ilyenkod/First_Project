from classic.app import DTO
from classic.components import component

from components.first_project_backend.chats.application import interfaces

class MessageInfo(DTO):
    text: str
    chat_id: int

class UserInfo(DTO):
    name: str
    password: str

class ChatInfo(DTO):
    title: str
    description: str

class ChatActionInfo(DTO):
    chat_id: int

class ChatUpdate(DTO):
    chat_id: int
    title: str
    description: str

class ChatAddUser(DTO):
    user_id: int
    chat_id: int

class UsersList(DTO):
    users: list

class MessageList(DTO):
    messages: list

class User_initiator(DTO):
    id: int



@component
class Users:

    users_repo: interfaces.UsersRepo

    def create_user(self, user_info: UserInfo):
        self.users_repo.create_user(user_info.name, user_info.password)


@component
class Chats:

    chats_repo: interfaces.ChatsRepo
    chat_repo: interfaces.ChatRepo

    def create_chat(self, chat_info: ChatInfo, user_id: User_initiator):
        self.chats_repo.create_chat(user_id.id, chat_info.title, chat_info.description)

    def delete_chat(self, chat_delete_info: ChatActionInfo, user_id: User_initiator):
        if self.chats_repo.is_owner(user_id.id, chat_delete_info.chat_id):
            self.chats_repo.delete_chat(user_id.id, chat_delete_info.chat_id)
        else:
            raise Exception("Нет прав для удаления")

    def get_len(self):
        return self.chats_repo.get_len()

    def update_information(self, chat_update: ChatUpdate, user_id: User_initiator):
        if self.chats_repo.is_owner(user_id.id, chat_update.chat_id):
            self.chats_repo.update_information(user_id.id, chat_update.chat_id,
                                          chat_update.title, chat_update.description)
        else:
            raise Exception("Пользователь не может редактировать чат")

    def add_user(self, information: ChatAddUser, user_id: User_initiator):
        if not self.chats_repo.is_owner(user_id.id, information.chat_id):
            raise Exception("Пользователь не может добавить в чат другого пользователя")
        elif self.chat_repo.is_participant(information.user_id, information.chat_id):
            raise Exception("Пользователь уже в чате")
        elif self.chat_repo.in_leave_list(information.user_id, information.chat_id):
            raise Exception("Пользователь сам покинул чат")
        else:
            self.chats_repo.add_user(user_id.id, information.user_id, information.chat_id)

    def delete_user(self, information: ChatAddUser, user_id: User_initiator):
        if not self.chats_repo.is_owner(user_id.id, information.chat_id):
            raise Exception("Пользователь не может удалить из чата другого пользователя")
        elif not self.chat_repo.is_participant(information.user_id, information.chat_id):
            raise Exception("Пользователь не состоит в чате")
        elif self.chat_repo.in_leave_list(information.user_id, information.chat_id):
            raise Exception("Пользователь сам покинул чат")
        else:
            self.chats_repo.kick_user(information.user_id, information.chat_id)


@component
class Chat:

    chat_repo: interfaces.ChatRepo

    def get_information(self, chat_init_info: ChatActionInfo, user_id: User_initiator):
        if self.chat_repo.is_participant(user_id.id, chat_init_info.chat_id):
            information = self.chat_repo.get_information(chat_init_info.chat_id, user_id.id)
            for_return = ChatInfo.parse_obj(information)
            return for_return
        else:
            raise Exception("Пользователь не может получить информацию о чате")

    def get_users(self, chat_in: ChatActionInfo, user_id: User_initiator):
        if self.chat_repo.is_participant(user_id.id, chat_in.chat_id):
            information = self.chat_repo.get_users(user_id.id, chat_in.chat_id)
            for_return = UsersList.parse_obj(information)
            return for_return
        else:
            raise Exception("Пользователь не может получить список участников чата")

    def send_message(self, message: MessageInfo, user_id: User_initiator):
        if self.chat_repo.is_participant(user_id.id, message.chat_id):
            self.chat_repo.send_message(user_id.id, message.text, message.chat_id)
        else:
            raise Exception("Пользователь не состоит в чате")

    def get_messages(self, message_info: ChatActionInfo, user_id: User_initiator):
        if self.chat_repo.is_participant(user_id.id, message_info.chat_id):
            information = self.chat_repo.get_messages(user_id.id, message_info.chat_id)
            for_return = MessageList.parse_obj(information)
            return for_return
        else:
            raise Exception("Пользователь не может получить список сообщений")

    def leave_chat(self, chat_action: ChatActionInfo, user_id: User_initiator):
        if self.chat_repo.is_participant(user_id.id, chat_action.chat_id):
            self.chat_repo.leave_chat(chat_action.chat_id, user_id.id)
        else:
            raise Exception("Пользователь не состоит в чате")

