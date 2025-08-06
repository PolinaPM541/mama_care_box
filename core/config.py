from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: Literal["TEST", "DEV", "PROD"]
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    GOOGLE_CLIENT_ID: str = "test_client_id"
    GOOGLE_CLIENT_SECRET: str = "test_client_secret"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
