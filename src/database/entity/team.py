from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.entity.base import BaseEntity


class Team(BaseEntity):
    __tablename__ = "teams"

    name: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)

    users: Mapped[list["User"]] = relationship("User", back_populates="team")
    vpn_configs: Mapped[list["VpnConfig"]] = relationship("VpnConfig", back_populates="team")
    vulnboxes: Mapped[list["Vulnbox"]] = relationship("Vulnbox", back_populates="team")
