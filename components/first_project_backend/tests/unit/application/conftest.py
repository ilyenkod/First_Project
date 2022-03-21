import pytest

from unittest.mock import Mock

from components.first_project_backend.chats.adapters.database import repositories
from components.first_project_backend.chats.application import services, interfaces


@pytest.fixture(scope='function')
def users_repo():
    users_repo = Mock(repositories.UsersRepo())
    users_repo.create_user = Mock()
    return users_repo

@pytest.fixture(scope='function')
def chats_repo():
    chats_repo = Mock(repositories.ChatsRepo())
    chats_repo.add_user = Mock()
    chats_repo.delete_chat = Mock()
    chats_repo.update_information = Mock()
    chats_repo.delete_user = Mock()
    return chats_repo


@pytest.fixture(scope='function')
def chat_repo(chat_information, messages_list, users_information):
    chat_repo = Mock(repositories.ChatRepo())
    chat_repo.get_information = Mock(return_value=chat_information)
    chat_repo.get_users = Mock(return_value=users_information)
    chat_repo.get_messages = Mock(return_value=messages_list)
    chat_repo.leave_chat = Mock()
    chat_repo.send_message = Mock()
    return chat_repo


@pytest.fixture(scope='function')
def service_chats(chats_repo, chat_repo):
    return services.Chats(chats_repo=chats_repo, chat_repo=chat_repo)

@pytest.fixture(scope='function')
def service_chat(chat_repo):
    return services.Chat(chat_repo=chat_repo)

