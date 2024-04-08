from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row, Start, SwitchTo
from aiogram_dialog.widgets.text import Const

from services.user.main import is_admin, render_rules, render_vulnboxes, send_vpn_configs
from views.admin.main.state import AdminMainStateGroup
from views.loader import load_template
from views.user.announcement.state import UserAnnouncementStateGroup
from views.user.main.state import UserMainStateGroup

menu = Window(
    Const("OmCTF Attack Defense Bot"),
    Row(
        Button(Const("VPN"), id="vpn", on_click=send_vpn_configs),
        SwitchTo(Const("Vuln Box"), id="vulnbox", state=UserMainStateGroup.vulnboxes),
        SwitchTo(Const("Rules"), id="rules", state=UserMainStateGroup.rules),
    ),
    Start(Const("Announcements"), id="announcements", state=UserAnnouncementStateGroup.announcements),
    Start(Const("Admin"), id="admin", state=AdminMainStateGroup.menu, when=is_admin),
    state=UserMainStateGroup.menu,
)

vulnboxes = Window(
    load_template("vulnboxes"),
    SwitchTo(Const("Back"), id="back", state=UserMainStateGroup.menu),
    state=UserMainStateGroup.vulnboxes,
    getter=render_vulnboxes,
)

rules = Window(
    load_template("rules"),
    SwitchTo(Const("Back"), id="back", state=UserMainStateGroup.menu),
    state=UserMainStateGroup.rules,
    getter=render_rules,
)
