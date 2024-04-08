import asyncio
from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from database.entity import Announcement, User
from database.session import DatabaseSessionManager
from views.admin.announcement.state import AdminAnnouncementGroup
from views.loader import load_template


async def select(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, item_id: int):
    with DatabaseSessionManager() as session:
        announcement = Announcement.find_by_id(session, item_id)
        dialog_manager.dialog_data["announcement"] = announcement
    await dialog_manager.switch_to(AdminAnnouncementGroup.announcement)


async def prompt_title(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data["announcement"] = dict()
    dialog_manager.dialog_data["announcement"]["title"] = message.text
    await dialog_manager.switch_to(AdminAnnouncementGroup.description)


async def prompt_description(message: Message, widget: MessageInput, dialog_manager: DialogManager):
    dialog_manager.dialog_data["announcement"]["description"] = message.text
    await dialog_manager.switch_to(AdminAnnouncementGroup.send)


async def render_announcement(dialog_manager: DialogManager, **kwargs):
    return {"announcement": dialog_manager.dialog_data["announcement"]}


async def send_announcement(callback: CallbackQuery, button: Button, manager: DialogManager):
    announcement = manager.dialog_data["announcement"]

    with DatabaseSessionManager() as session:
        tg_ids = [user.tg_id for user in User.find_all(session)]
        Announcement.create(session, **announcement)

    message = await load_template("announcement").render_text({"announcement": announcement}, manager)

    await manager.done()
    tasks = [callback.bot.send_message(tg_id, message) for tg_id in tg_ids]
    await asyncio.gather(*tasks)
