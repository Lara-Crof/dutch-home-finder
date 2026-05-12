from urllib.parse import urlencode
from datetime import datetime, timedelta, timezone
from pydantic_settings import BaseSettings, SettingsConfigDict


class RequestsSettings(BaseSettings):
    requests_timeout: int
    requests_interval: int
    requests_url: str
    requests_proxy_host: str
    requests_proxy_port: int
    requests_proxy_user: str
    requests_proxy_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf8",
        extra="ignore",
    )


class FundaSettings(RequestsSettings):
    funda_requests_url: str
    funda_city: str
    funda_min_price: int
    funda_max_price: int
    funda_property_type: str
    funda_publication_days: int
    funda_listing_status: str
    funda_sort: str
    funda_radius_km: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf8",
        extra="ignore",
    )

    @property
    def offset_days(self):
        offset_days = datetime.now().date() - timedelta(
            days=self.funda_publication_days
        )
        return offset_days

    @property
    def get_publication_cutoff(self) -> datetime:
        return datetime.now(timezone.utc) - timedelta(
            days=self.funda_publication_days
        )
