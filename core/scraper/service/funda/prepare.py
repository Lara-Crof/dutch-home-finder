from datetime import datetime, timezone
from typing import Any

from config.settings import settings
from core.scraper.enums import HouseStatus
from core.scraper.service.base_prepare.base_prepare import ListingPreparerBase

from core.scraper.service.funda.schemas import (
    ObjectHouseInfo,
    HouseStorageInfoSave,
)


class FundaListingPreparer(ListingPreparerBase):
    def prepare_for_telegram(self, listing: Any) -> ObjectHouseInfo:
        return ObjectHouseInfo(
            status=self.resolve_status(listing),
            price=int(listing.price.amount),
            area=listing.living_area,
            rooms=listing.rooms_count,
            city=listing.city,
            district=self.format_full_address(listing.address),
            energy_label=listing.energy_label,
            listed_at=listing.publication_date,
            source_url=listing.url,
        )

    def prepare_for_storage(self, listing: Any) -> HouseStorageInfoSave:
        return HouseStorageInfoSave(
            listing_id=listing.id,
            status=self.resolve_status(listing),
            source_url=listing.url,
            listed_at=listing.publication_date,
        )

    def resolve_status(self, listing: Any):
        result = HouseStatus.OLD_PUBLISHED

        if listing.status == "available":
            publication_date = datetime.strptime(
                listing.publication_date.replace("Z", ""),
                "%Y-%m-%dT%H:%M:%S",
            ).replace(tzinfo=timezone.utc)

            if publication_date > settings.funda_settings.get_publication_cutoff:
                result = HouseStatus.RECENTLY_PUBLISHED
            else:
                result = HouseStatus.OLD_PUBLISHED

        return result

    def format_full_address(self, address: Any) -> str:
        return f"{address.title}, {address.postcode} {address.city}"