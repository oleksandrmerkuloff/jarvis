from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.expression import func


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )
