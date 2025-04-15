from typing import Optional, Union

from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class Task(Base):
    __tablename__ = 'tasks'
