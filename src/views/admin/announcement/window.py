from operator import attrgetter

from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, ScrollingGroup, Select, SwitchTo, Url
from aiogram_dialog.widgets.text import Const, Format

from services.admin.announcement import prompt_description, prompt_title, render_announcement, select, send_announcement
from services.user.announcement import list_all, render
from views.admin.announcement.state import AdminAnnouncementGroup
from views.loader import load_template

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
    Row(
        Cancel(Const("Back"), id="back"),
        SwitchTo(Const("Add"), id="add", state=AdminAnnouncementGroup.title),
    ),
    getter=list_all,
    state=AdminAnnouncementGroup.announcements,
)

announcement = Window(
    load_template("announcement"),
    Row(
        SwitchTo(Const("Back"), id="back", state=AdminAnnouncementGroup.announcements),
        Url(
            Const("Edit"),
            Const("https://github.com"),
        ),
    ),
    state=AdminAnnouncementGroup.announcement,
    getter=render,
)

title = Window(
    Const("Enter title:"),
    MessageInput(prompt_title),
    Row(
        SwitchTo(Const("Back"), id="back", state=AdminAnnouncementGroup.announcements),
        Cancel(Const("Cancel"), id="cancel"),
    ),
    state=AdminAnnouncementGroup.title,
)

description = Window(
    Const("Enter description:"),
    MessageInput(prompt_description),
    Row(
        SwitchTo(Const("Back"), id="back", state=AdminAnnouncementGroup.title),
        Cancel(Const("Cancel"), id="cancel"),
    ),
    state=AdminAnnouncementGroup.description,
)

send = Window(
    load_template("announcement"),
    Button(Const("Send"), id="send", on_click=send_announcement),
    Row(
        SwitchTo(Const("Back"), id="back", state=AdminAnnouncementGroup.description),
        Cancel(Const("Cancel"), id="cancel"),
    ),
    state=AdminAnnouncementGroup.send,
    getter=render_announcement,
)
