from aiogram.fsm.state import State, StatesGroup


class UserMainStateGroup(StatesGroup):
    menu = State()
    rules = State()
    vulnboxes = State()
    announcements = State()
    announcement = State()
