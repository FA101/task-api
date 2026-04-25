"""Ponto de entrada da aplicação FastAPI — Task API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.task_controller import router as task_router
from app.core.config import settings
from app.core.database import engine
from app.models.task import Base

# Criação automática das tabelas (dev/MVP — em produção use Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API RESTful para gerenciamento de tarefas com FastAPI e PostgreSQL.",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)


@app.get("/health", tags=["health"])
def health_check():
    """Smoke test: verifica se a API está no ar."""
    return {"status": "ok", "version": settings.APP_VERSION}
