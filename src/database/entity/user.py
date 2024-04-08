from __future__ import annotations

from typing import Sequence

from sqlalchemy import ForeignKey, String, select
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from database.entity import Team
from database.entity.base import BaseEntity


class User(BaseEntity):
    __tablename__ = "users"

    tg_id: Mapped[str] = mapped_column(String(16), nullable=False, unique=True)
    admin: Mapped[bool] = mapped_column(nullable=False, default=False)
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.id), nullable=True)

    team: Mapped[Team] = relationship(Team, back_populates="users")

    @classmethod
    def find_by_tg_id(cls, session: Session, tg_id: int) -> User | None:
        statement = select(cls).where(cls.tg_id == tg_id)
        return session.scalars(statement).first()

    @classmethod
    def find_all(cls, session: Session) -> Sequence[User]:
        statement = select(cls)
        return session.scalars(statement).all()
