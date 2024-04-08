from aiogram_dialog import Dialog

from controller.dispatcher import dp
from views.admin.main import window


def main_dialog():
    dialog = Dialog(
        window.menu,
    )
    dp.include_router(dialog)
