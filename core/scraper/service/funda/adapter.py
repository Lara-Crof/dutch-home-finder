from core.scraper.repository import HouseStorageInfoManager
from core.scraper.service.funda.client import FundaClient
from core.scraper.service.funda.filters import ListingStatusFilter, PublicationDateFilter
from core.scraper.service.funda.prepare import FundaListingPreparer
from core.scraper.service.funda.utils import parse_date


class FundaNewListingsService:
    def __init__(self):
        self.client = FundaClient()
        self.storage_manager = HouseStorageInfoManager()
        self.preparer = FundaListingPreparer()
        self.status_filter = ListingStatusFilter()
        self.date_filter = PublicationDateFilter()

    async def collect_new_listings(self):
        candidates = await self.__fetch_listings()
        new_listing_ids = await self.__filter_out_stored_listing_ids(candidates)
        listing_details = await self.__fetch_listing_details(new_listing_ids)

        active_listings = self.status_filter.apply(listing_details)
        fresh_listings = self.date_filter.apply(active_listings)

        fresh_listings.sort(
            key=lambda listing: parse_date(listing.publication_date),
            reverse=True,
        )

        return self.preparer.prepare_all_listings(fresh_listings)

    async def __fetch_listings(self):
        return self.client.search()

    async def __filter_out_stored_listing_ids(self, listings):
        listing_ids = [listing.id for listing in listings]
        return await self.storage_manager.collect_new_listing_ids(candidate_listing_ids=listing_ids)

    async def __fetch_listing_details(self, listing_ids):
        return [self.client.get_listing(listing_id) for listing_id in listing_ids]
