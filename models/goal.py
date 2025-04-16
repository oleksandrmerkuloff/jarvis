from typing import List

from sqlalchemy import String, Text, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from base import Base
from task import Task
from mixins.time_mixin import TimestampMixin


class Goal(Base, TimestampMixin):
    __tablename__ = 'goals'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=True)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)

    tasks: Mapped[List['Task']] = relationship(back_populates='goal')

    def __str__(self):
        return self.name

    def __repr__(self):
        report = 'Title: ' + self.name + '\n'
        report += f'Created at: {self.created_at:%Y/%m/%d %H:%M:%S}\n'
        report += f'Last update: {self.updated_at:%Y/%m/%d %H:%M:%S}'
        return report
