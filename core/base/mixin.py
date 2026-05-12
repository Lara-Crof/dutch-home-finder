import datetime
import uuid

from sqlalchemy import UUID, func, DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class UUIDMixin:
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )


class TimestampsMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        default=datetime.datetime.now,
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )
