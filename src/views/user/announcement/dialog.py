from aiogram_dialog import Dialog

from controller.dispatcher import dp
from views.user.announcement import window


def announcements_dialog():
    dialog = Dialog(
        window.announcements,
        window.announcement,
    )
    dp.include_router(dialog)
