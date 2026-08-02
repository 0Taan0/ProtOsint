"""Konfiguration. Alle Keys optional -> Tool laeuft auch ohne HIBP-Key,
nur mit weniger Quellen. Wichtig fuer die GitHub-Version."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://footprint:footprint@localhost:5432/footprint"
    # Connector-Keys, alle optional:
    hibp_api_key: str | None = None
    openai_api_key: str | None = None
    # LLM:
    llm_model: str = "gpt-4o-mini"
    # Verhalten:
    offline: bool = False
    default_max_depth: int = 2
    default_budget_cents: int = 100

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
