from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from base import Base
from mixins.time_mixin import TimestampMixin


class Note(Base, TimestampMixin):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        report = 'Title: ' + self.title + '\n'
        report += f'Created at: {self.created_at:%Y/%m/%d %H:%M}'
        return report
