from pydantic import SecretStr
from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: SecretStr
    db_echo: bool

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf8",
        extra="ignore",
    )

    @property
    def build_db_url(self) -> str:
        try:
            url_connection_string = (
                f"postgresql+asyncpg://{self.db_user}:{self.db_password.get_secret_value()}"
                f"@{self.db_host}:{self.db_port}/{self.db_name}"
            )
            return url_connection_string
        except Exception as e:
            raise ValueError(f"Failed to build database URL: {e}")
