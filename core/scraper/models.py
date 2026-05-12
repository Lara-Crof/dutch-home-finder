import datetime

from sqlalchemy import DateTime, Enum, String
from sqlalchemy.orm import mapped_column, Mapped

from core.base.mixin import TimestampsMixin, UUIDMixin
from core.base.models import Base
from core.scraper.enums import HouseStatus
from core.scraper.service.funda.schemas import HouseStorageInfoSave


class HouseStorageInfo(UUIDMixin, TimestampsMixin, Base):
    status: Mapped[HouseStatus] = mapped_column(Enum(HouseStatus), nullable=False)
    source_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    listed_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    listing_id: Mapped[str] = mapped_column(String(255), nullable=False)
