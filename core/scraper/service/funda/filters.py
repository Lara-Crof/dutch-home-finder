from config.settings import settings
from core.scraper.service.funda.utils import parse_date


class PublicationDateFilter:
    def __init__(self):
        self.cutoff = settings.funda_settings.get_publication_cutoff

    def apply(self, listings):
        filtered = []

        for listing in listings:
            if parse_date(listing.publication_date) >= self.cutoff:
                filtered.append(listing)

        return filtered


class ListingStatusFilter:
    def __init__(self):
        self.excluded_types = {"TransactionStatus"}

    def apply(self, listings):
        filtered = []

        for listing in listings:
            has_excluded_status = any(
                label.type in self.excluded_types
                for label in listing.labels
            )

            if not has_excluded_status:
                filtered.append(listing)

        return filtered
