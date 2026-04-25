"""Configurações centralizadas carregadas do arquivo .env."""

import os

os.environ["LANG"] = "en_US.UTF-8"
os.environ["PGLOCALEDIR"] = ""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Variáveis de ambiente da aplicação."""

    APP_NAME: str = "Task API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    DATABASE_URL: str = "postgresql://postgres:12345@localhost:5432/taskdb"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()