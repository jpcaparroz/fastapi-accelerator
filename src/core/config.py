from typing import ClassVar

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from sqlalchemy.orm import declarative_base
from sqlalchemy import URL

from utils import get_env
from utils import get_env_database_config


class Settings(BaseSettings):
    """
    General configs
    """
    API_VERSION_ADDRESS: str = '/api/v1'
    DB_URL: URL = URL.create(**get_env_database_config())
    DBBaseModel: ClassVar = declarative_base()
    JWT_SECRET: str = get_env('SECURITY_JWT_SECRET')
    ALGORITHM: str = get_env('SECURITY_ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = get_env('SECURITY_TOKEN_EXPIRE_MINUTES')

    model_config = SettingsConfigDict(case_sensitive=True)


settings: Settings = Settings()