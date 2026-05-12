from abc import ABC, abstractmethod
from typing import Any


class ListingPreparerBase(ABC):
    def prepare_all_listings(self, listings: list[Any]) -> tuple[list, list]:
        telegram_objects = []
        storage_objects = []

        for listing in listings:
            telegram_objects.append(self.prepare_for_telegram(listing))
            storage_objects.append(self.prepare_for_storage(listing))

        return telegram_objects, storage_objects

    @abstractmethod
    def prepare_for_telegram(self, listing: Any):
        pass

    @abstractmethod
    def prepare_for_storage(self, listing: Any):
        pass