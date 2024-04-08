from aiogram_dialog import setup_dialogs

from controller.dispatcher import dp
from controller.routers.main import main_router


def register_routers():
    dp.include_router(main_router)
    setup_dialogs(dp)
