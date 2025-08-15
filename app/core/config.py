"""
Конфигурация приложения TrackMind
Использует Pydantic Settings для типобезопасной работы с переменными окружения
"""

import os
from functools import lru_cache

from pydantic import BaseSettings, Field, field_validator, PostgresDsn, RedisDsn, AnyHttpUrl
from pydantic.types import SecretStr


class DatabaseSettings(BaseSettings):
    """Настройки базы данных"""

    # PostgreSQL
    postgres_host: str = Field(default="localhost", env="POSTGRES_HOST")
    postrgres_port: int = Field(default=5432, env="POSTGRES_PORT")
    postgres_user: str = Field(default="postgres", env="POSTGRES_USER")
    postgres_password: SecretStr = Field(default=SecretStr("12345678"), env="POSTGRES_PASSWORD")
    postgres_db: str = Field(default="trackmind", env="POSTGRES_DB")
    postgres_pool_size: int = Field(default=10, env="POSTGRES_POOL_SIZE")
    postgres_max_overflow: int = Field(default=20, env="POSTGRES_MAX_OVERFLOW")

    @property
    def postgres_url(self) -> str:
         """URL для подключения к PostgreSQL"""
         return (
            f"postgresql://{self.postgres_user}:{self.postgres_password.get_secret_value()}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
         )

    class Config:
        emv_prefix = "DB_"


class Settings(BaseSettings):
    """Основные настройки приложения"""

    # Окружение
    environment: str = Field(default="development", env="ENVIRONMENT")
    debug: bool = Field(default=True, env="DEBUG")

    # Поднастройки
    database: DatabaseSettings = DatabaseSettings()

    @field_validator("enviroment")
    @classmethod
    def validate_environment(cls, v):
        """Валидация окружения"""
        allowed = ['development', 'staging', 'production', 'testing']
        if v not in allowed:
            raise ValueError(f"Invalid environment: {v}. Allowed values are: {allowed}")
        return v

    @property
    def is_development(self) -> bool:
        """Проверка на окружение development"""
        return self.environment == "development"
    
    @property
    def is_production(self) -> bool:
        """Проверка на окружение production"""
        return self.environment == "production"
    
    @property
    def is_testing(self) -> bool:
        """Проверка на testing окружение"""
        return self.environment == "testing"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()