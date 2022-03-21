import pytest

from components.first_project_backend.chats.application import services

@pytest.fixture(scope='function')
def chat_information():
    return services.ChatInfo(
        title="Title",
    description="Decription"
    )

@pytest.fixture(scope='function')
def users_information():
    return services.UsersList(
        users=["user1", "user2"]
    )

@pytest.fixture(scope='function')
def messages_list():
    return services.MessageList(
        messages=["mes1", "mes2"]
    )

@pytest.fixture(scope="function")
def for_users_create():
    return ["user1", "user2"]

