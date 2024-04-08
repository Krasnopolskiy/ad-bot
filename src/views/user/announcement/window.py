from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, ScrollingGroup, Select, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from services.user.announcement import list_all, render, select
from views.loader import load_template
from views.user.announcement.state import UserAnnouncementStateGroup

announcements = Window(
    load_template("announcements"),
    ScrollingGroup(
        Select(
            Format("{item.title}"),
            item_id_getter=attrgetter("id"),
            items="announcements",
            id="announcement_select",
            on_click=select,
        ),
        width=1,
        height=5,
        id="announcement_group",
    ),
    Cancel(Const("Back"), id="back"),
    getter=list_all,
    state=UserAnnouncementStateGroup.announcements,
)

announcement = Window(
    load_template("announcement"),
    SwitchTo(Const("Back"), id="back", state=UserAnnouncementStateGroup.announcements),
    state=UserAnnouncementStateGroup.announcement,
    getter=render,
)
