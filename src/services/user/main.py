from aiogram.types import CallbackQuery, Message
from aiogram.types import User as TgUser
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable
from aiogram_dialog.widgets.kbd import Button

from config.s3 import S3Config
from database.entity import Rule, User
from database.session import DatabaseSessionManager


def is_admin(data: dict, widget: Whenable, manager: DialogManager):
    with DatabaseSessionManager() as session:
        message: Message = data["event"]
        user = User.find_by_tg_id(session, message.from_user.id)
        return user.admin


async def send_vpn_configs(callback: CallbackQuery, button: Button, manager: DialogManager):
    with DatabaseSessionManager() as session:
        user = User.find_by_tg_id(session, callback.from_user.id)
        configs = user.team.vpn_configs
    s3 = S3Config()
    items = [s3.read_document(config.path) for config in configs]
    if len(items) > 0:
        await callback.bot.send_media_group(chat_id=callback.message.chat.id, media=items)


async def render_vulnboxes(event_from_user: TgUser, **kwargs):
    with DatabaseSessionManager() as session:
        user = User.find_by_tg_id(session, event_from_user.id)
        return {"vulnboxes": [vulnbox.description for vulnbox in user.team.vulnboxes]}


async def render_rules(**kwargs):
    with DatabaseSessionManager() as session:
        rules = Rule.find_all(session)
        return {"rules": [rule.description for rule in rules]}
