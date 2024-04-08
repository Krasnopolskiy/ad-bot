from __future__ import annotations

from typing import Sequence

from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, Session, mapped_column

from database.entity.base import BaseEntity


class Rule(BaseEntity):
    __tablename__ = "rules"

    description: Mapped[str] = mapped_column(String(4096), nullable=False)

    @classmethod
    def find_all(cls, session: Session) -> Sequence[Rule]:
        statement = select(cls)
        return session.scalars(statement).all()
