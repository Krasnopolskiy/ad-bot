from aiogram.fsm.state import State, StatesGroup


class UserAnnouncementStateGroup(StatesGroup):
    announcements = State()
    announcement = State()
