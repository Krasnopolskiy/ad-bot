from aiogram.types import Message

from database.entity import User
from database.session import DatabaseSessionManager


async def is_invited(message: Message):
    with DatabaseSessionManager() as session:
        user = User.find_by_tg_id(session, message.from_user.id)
        return user is not None


async def is_admin(message: Message):
    with DatabaseSessionManager() as session:
        user = User.find_by_tg_id(session, message.from_user.id)
        return user is not None and user.admin
