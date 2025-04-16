from sqlalchemy import String, Text, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from base import Base
from goal import Goal
from mixins.time_mixin import TimestampMixin


class Task(Base, TimestampMixin):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=True)
    is_done: Mapped[bool] = mapped_column(Boolean, default=False)
    goal_id: Mapped[int] = mapped_column(
        ForeignKey('goals.id', ondelete='CASCADE'),
        nullable=True,
        )

    goal: Mapped['Goal'] = relationship(back_populates='tasks')

    def __str__(self):
        return self.name

    def __repr__(self):
        report = 'Title: ' + self.name + '\n'
        report += f'Created at: {self.created_at:%Y/%m/%d %H:%M}\n'
        report += f'Last update: {self.updated_at:%Y/%m/%d %H:%M}'
        return report
