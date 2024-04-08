from aiogram_dialog import Dialog

from controller.dispatcher import dp
from views.user.main import window


def main_dialog():
    dialog = Dialog(
        window.menu,
        window.vulnboxes,
        window.rules,
    )
    dp.include_router(dialog)
