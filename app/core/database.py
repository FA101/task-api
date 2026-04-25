"""Configuração da conexão com o PostgreSQL via SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=settings.DEBUG,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependência FastAPI: fornece e fecha a sessão do banco de dados."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
