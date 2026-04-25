"""Controller: define os endpoints RESTful para /tasks."""

from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.task_repository import TaskRepository
from app.schemas.task import Task, TaskCreate, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


def _get_service(db: Session = Depends(get_db)) -> TaskService:
    """Fábrica de TaskService com injeção de dependência."""
    return TaskService(TaskRepository(db))


@router.get("/", response_model=list[Task], summary="Listar tarefas")
def list_tasks(
    status: bool | None = Query(default=None, description="Filtrar por status"),
    service: TaskService = Depends(_get_service),
):
    """Retorna todas as tarefas. Use `?status=true` ou `?status=false` para filtrar."""
    return service.list_tasks(status=status)


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED, summary="Criar tarefa")
def create_task(payload: TaskCreate, service: TaskService = Depends(_get_service)):
    """Cria uma nova tarefa e retorna o recurso criado."""
    return service.create_task(payload)


@router.get("/{task_id}", response_model=Task, summary="Buscar tarefa")
def get_task(task_id: UUID, service: TaskService = Depends(_get_service)):
    """Retorna uma tarefa pelo seu UUID."""
    return service.get_task(task_id)


@router.put("/{task_id}", response_model=Task, summary="Atualizar tarefa")
def update_task(
    task_id: UUID,
    payload: TaskUpdate,
    service: TaskService = Depends(_get_service),
):
    """Atualiza parcialmente os campos de uma tarefa."""
    return service.update_task(task_id, payload)


@router.patch("/{task_id}/complete", response_model=Task, summary="Concluir tarefa")
def complete_task(task_id: UUID, service: TaskService = Depends(_get_service)):
    """Marca uma tarefa como concluída (status = true)."""
    return service.complete_task(task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Excluir tarefa")
def delete_task(task_id: UUID, service: TaskService = Depends(_get_service)):
    """Remove permanentemente uma tarefa."""
    service.delete_task(task_id)
