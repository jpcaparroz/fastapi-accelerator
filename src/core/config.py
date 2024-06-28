from typing import ClassVar

from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import URL

from utils import get_config


class Settings(BaseSettings):
    """
    General configs
    """
    API_VERSION_ADDRESS: str = '/api/v1'
    DB_URL: URL = URL.create(**get_config('database'))
    DBBaseModel: ClassVar = declarative_base()
    JWT_SECRET: str = get_config('security', 'jwt_secret')
    ALGORITHM: str = get_config('security', 'algorithm')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = get_config('security', 'token_expire_minutes')
    
    class Config:
        # important to follow
        case_sensitive = True


settings: Settings = Settings()