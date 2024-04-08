from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Start
from aiogram_dialog.widgets.text import Const

from views.admin.announcement.state import AdminAnnouncementGroup
from views.admin.main.state import AdminMainStateGroup

menu = Window(
    Const("!!! Admin Panel !!!\nOmCTF Attack Defense Bot"),
    Start(Const("Announcements"), id="announcements", state=AdminAnnouncementGroup.announcements),
    Cancel(Const("Back"), id="back"),
    state=AdminMainStateGroup.menu,
)
