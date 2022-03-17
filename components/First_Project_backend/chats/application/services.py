from classic.components import component

from dataclasses import User, Chat, Message

import interfaces

@component
class Users:

    users_repo: interfaces.UsersRepo

