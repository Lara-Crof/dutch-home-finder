from config.settings import settings
from funda import Funda


class FundaClient:
    def __init__(self):
        self._client = Funda()
        self._max_price = settings.funda_settings.funda_max_price
        self._city = settings.funda_settings.funda_city.lower()
        self._property_type = settings.funda_settings.funda_property_type
        self._radius_km = settings.funda_settings.funda_radius_km
        self._sorted = settings.funda_settings.funda_sort

    def __enter__(self):
        self._client.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.__exit__(exc_type, exc_val, exc_tb)

    def get_listing(self, listing_id):
        return self._client.listing(listing_id)

    def search(self):
        return self._client.search(
            max_price=self._max_price,
            location=self._city,
            object_type=self._property_type,
            sort=self._sorted,
            radius_km=self._radius_km,
        )
