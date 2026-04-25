"""Service: lógica de negócio para gerenciamento de tarefas."""

from uuid import UUID

from fastapi import HTTPException, status

from app.models.task import TaskModel
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    """Orquestra regras de negócio entre Controller e Repository."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repo = repository

    def list_tasks(self, status: bool | None = None) -> list[TaskModel]:
        """Lista tarefas com filtro opcional por status."""
        return self._repo.get_all(status=status)

    def get_task(self, task_id: UUID) -> TaskModel:
        """Retorna tarefa ou levanta HTTP 404."""
        task = self._repo.get_by_id(task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tarefa {task_id} não encontrada.",
            )
        return task

    def create_task(self, payload: TaskCreate) -> TaskModel:
        """Cria e persiste uma nova tarefa."""
        return self._repo.create(payload)

    def update_task(self, task_id: UUID, payload: TaskUpdate) -> TaskModel:
        """Atualiza campos de uma tarefa existente."""
        task = self.get_task(task_id)
        return self._repo.update(task, payload)

    def complete_task(self, task_id: UUID) -> TaskModel:
        """Marca uma tarefa como concluída (status = True)."""
        task = self.get_task(task_id)
        return self._repo.update(task, TaskUpdate(status=True))

    def delete_task(self, task_id: UUID) -> None:
        """Remove uma tarefa existente."""
        task = self.get_task(task_id)
        self._repo.delete(task)
