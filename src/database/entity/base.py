from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class BaseEntity(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @classmethod
    def find_by_id(cls, session: Session, _id: int):
        return session.query(cls).get(_id)
