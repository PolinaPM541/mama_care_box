from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["TEST", "DEV", "PROD"]
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    GOOGLE_CLIENT_ID: str = "test_client_id"
    GOOGLE_CLIENT_SECRET: str = "test_client_secret"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
