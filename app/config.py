from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["TEST", "DEV", "PROD"]
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    SECRETS: str
    COOKIE_MAX_AGE: int
    JWT_LIFETIME_SECONDS: int

    FACEBOOK_OAUTH2_CLIENT_ID: str
    FACEBOOK_OAUTH2_CLIENT_SECRET: str

    GOOGLE_OAUTH2_CLIENT_ID: str
    GOOGLE_OAUTH2_CLIENT_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
