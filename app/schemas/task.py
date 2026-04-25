"""Schemas Pydantic para validação e serialização de tarefas."""

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    """Campos compartilhados entre criação e leitura."""

    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Título da tarefa (3–100 caracteres).",
    )
    description: str | None = Field(
        default=None,
        description="Descrição opcional da tarefa.",
    )


class TaskCreate(TaskBase):
    """Schema para criação de uma nova tarefa (sem id nem timestamps)."""

    pass


class TaskUpdate(BaseModel):
    """Schema para atualização parcial (todos os campos opcionais)."""

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
        description="Novo título da tarefa.",
    )
    description: str | None = Field(
        default=None,
        description="Nova descrição da tarefa.",
    )
    status: bool | None = Field(
        default=None,
        description="Novo status da tarefa (True = concluída).",
    )


class Task(TaskBase):
    """Schema completo retornado pela API."""

    id: UUID = Field(
        default_factory=uuid4,
        description="Identificador único da tarefa (UUID v4).",
    )
    status: bool = Field(
        default=False,
        description="Status da tarefa: False = pendente, True = concluída.",
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Data e hora de criação (UTC).",
    )

    model_config = {"from_attributes": True}
