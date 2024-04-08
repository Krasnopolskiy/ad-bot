from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from database.entity import Announcement
from database.session import DatabaseSessionManager
from views.user.announcement.state import UserAnnouncementStateGroup


async def list_all(**kwargs):
    with DatabaseSessionManager() as session:
        announcement = Announcement.find_all(session)
        return {"announcements": announcement}


async def select(callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, item_id: int):
    with DatabaseSessionManager() as session:
        announcement = Announcement.find_by_id(session, item_id)
        dialog_manager.dialog_data["announcement"] = announcement
    await dialog_manager.switch_to(UserAnnouncementStateGroup.announcement)


async def render(dialog_manager: DialogManager, **kwargs):
    announcement = dialog_manager.dialog_data["announcement"]
    return {"announcement": announcement}
