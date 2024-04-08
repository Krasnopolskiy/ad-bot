from __future__ import annotations

from typing import Sequence

from sqlalchemy import ForeignKey, String, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.entity import Team
from database.entity.base import BaseEntity
from database.session import DatabaseSessionManager


class VpnConfig(BaseEntity):
    __tablename__ = "vpn_configs"

    path: Mapped[str] = mapped_column(String(128), nullable=False)
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.id), nullable=False)

    team: Mapped[Team] = relationship(Team, back_populates="vpn_configs")

    @classmethod
    def find_by_team_id(cls, team_id: int) -> Sequence[VpnConfig]:
        with DatabaseSessionManager() as session:
            statement = select(VpnConfig).where(VpnConfig.team_id == team_id)
            return session.scalars(statement).all()
