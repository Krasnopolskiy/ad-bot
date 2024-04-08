from aiogram_dialog import Dialog

from controller.dispatcher import dp
from views.admin.announcement import window


def announcements_dialog():
    dialog = Dialog(
        window.announcements,
        window.announcement,
        window.title,
        window.description,
        window.send,
    )
    dp.include_router(dialog)
