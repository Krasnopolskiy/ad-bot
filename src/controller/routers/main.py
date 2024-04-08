from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from controller.filters import is_invited
from views.user.main.state import UserMainStateGroup

main_router = Router(name=__name__)
main_router.message.filter(is_invited)


@main_router.message(CommandStart())
async def start_main_dialog(_: Message, dialog_manager: DialogManager):
    await dialog_manager.start(UserMainStateGroup.menu, mode=StartMode.NORMAL)
