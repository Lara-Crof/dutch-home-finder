from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl

from core.scraper.enums import HouseStatus


class ObjectHouseInfo(BaseModel):
    status: HouseStatus

    price: int
    area: float
    rooms: int

    city: str
    district: str
    # district_rating: float

    # construction_year: int
    energy_label: str | None = None
    listed_at: datetime
    source_url: str


class HouseStorageInfoSave(BaseModel):
    listing_id: str
    status: str
    source_url: str
    listed_at: datetime
    listed_at: datetime
