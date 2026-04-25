"""Configurações centralizadas carregadas do arquivo .env."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Variáveis de ambiente da aplicação."""

    APP_NAME: str = "Task API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/taskdb"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
