from pydantic_settings import BaseSettings

from config.settings_db import DBSettings
from config.settings_requests import RequestsSettings, FundaSettings
from config.settings_telegram import TelegramSettings


class Settings(BaseSettings):
    db_settings: DBSettings = DBSettings()
    tg_settings: TelegramSettings = TelegramSettings()
    requests_settings: RequestsSettings = RequestsSettings()
    funda_settings: FundaSettings = FundaSettings()


settings = Settings()
