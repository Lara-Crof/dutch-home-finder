from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict, BaseSettings


class TelegramSettings(BaseSettings):
    telegram_token_bot: SecretStr
    telegram_chat_id: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf8",
        extra="ignore",
    )
