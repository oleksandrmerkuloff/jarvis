from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, Text, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


# class Theme(Base):
#     __tablename__ = 'themes'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(50), nullable=False)

#     def __str__(self) -> str:
#         return self.name.title()


class Goal(Base):
    __tablename__ = 'goals'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        nullable=False
        )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="goal",
        cascade="all, delete",
        passive_deletes=True,
        )

    def __str__(self) -> str:
        """
        Return title to user
        """
        return self.name


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    text: Mapped[str] = mapped_column(Text)
    is_done: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
        )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        nullable=False
        )
    goal_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("goals.id", ondelete="CASCADE"),
        nullable=False
        )

    goal: Mapped[Optional["Goal"]] = relationship(back_populates="tasks")

    def __str__(self) -> str:
        """
        Return title to user
        """
        return self.title

    def __repr__(self) -> str:
        """
        Return title with last update date for tech purposes
        """
        return self.title + '\nCreated at: ' + self.created_at


class Note(Base):
    __table__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        nullable=False
        )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    def __str__(self) -> str:
        """
        Return title to user
        """
        return self.title

    def __repr__(self) -> str:
        """
        Return title with last update date for tech purposes
        """
        return self.title + '\nLast update at: ' + self.updated_at
