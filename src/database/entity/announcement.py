from __future__ import annotations

from datetime import datetime
from typing import Sequence

from sqlalchemy import String, func, select
from sqlalchemy.orm import Mapped, Session, mapped_column

from database.entity.base import BaseEntity


class Announcement(BaseEntity):
    __tablename__ = "announcements"

    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(4096), nullable=False)

    @classmethod
    def find_all(cls, session: Session) -> Sequence[Announcement]:
        statement = select(cls).order_by(cls.created_at.desc())
        return session.scalars(statement).all()

    @classmethod
    def create(cls, session: Session, title: str, description: str) -> Announcement:
        announcement = Announcement(title=title, description=description)
        session.add(announcement)
        session.commit()
        return announcement
