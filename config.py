from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    lm_studio_base_url: str = "http://localhost:1234/v1"
    model: str = "qwen"
    temperature: float = 0.7
    database_url: str = "budget.db"
    openrouter_api_key: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()