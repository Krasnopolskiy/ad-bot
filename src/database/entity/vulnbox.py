from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.entity import Team
from database.entity.base import BaseEntity


class Vulnbox(BaseEntity):
    __tablename__ = "vulnboxes"

    description: Mapped[str] = mapped_column(String(1024), nullable=False)
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.id), nullable=False)

    team: Mapped[Team] = relationship(Team, back_populates="vulnboxes")
