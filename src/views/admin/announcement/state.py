from aiogram.fsm.state import State, StatesGroup


class AdminAnnouncementGroup(StatesGroup):
    menu = State()
    announcements = State()
    announcement = State()
    title = State()
    description = State()
    send = State()
