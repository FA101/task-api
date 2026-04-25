"""Repository: encapsula todas as queries SQL para a tabela tasks."""

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.task import TaskModel
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository:
    """Gerencia o acesso ao banco de dados para tarefas (DRY, SOLID)."""

    def __init__(self, db: Session) -> None:
        self._db = db

    def get_all(self, status: bool | None = None) -> list[TaskModel]:
        """Retorna todas as tarefas, com filtro opcional por status."""
        query = self._db.query(TaskModel)
        if status is not None:
            query = query.filter(TaskModel.status == status)
        return query.order_by(TaskModel.created_at.desc()).all()

    def get_by_id(self, task_id: UUID) -> TaskModel | None:
        """Retorna uma tarefa pelo UUID ou None se não encontrada."""
        return self._db.query(TaskModel).filter(TaskModel.id == task_id).first()

    def create(self, payload: TaskCreate) -> TaskModel:
        """Persiste uma nova tarefa e retorna o objeto criado."""
        task = TaskModel(**payload.model_dump())
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)
        return task

    def update(self, task: TaskModel, payload: TaskUpdate) -> TaskModel:
        """Atualiza os campos fornecidos (atualização parcial)."""
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(task, field, value)
        self._db.commit()
        self._db.refresh(task)
        return task

    def delete(self, task: TaskModel) -> None:
        """Remove a tarefa do banco de dados."""
        self._db.delete(task)
        self._db.commit()
