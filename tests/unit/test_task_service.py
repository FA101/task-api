"""Testes unitários para TaskService (padrão TDD: red → green → refactor)."""

from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from fastapi import HTTPException

from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import TaskService


@pytest.fixture
def mock_repo():
    """Repositório simulado (mock) para isolar o Service."""
    return MagicMock()


@pytest.fixture
def service(mock_repo):
    """Instância do TaskService com repositório mock."""
    return TaskService(mock_repo)


class TestListTasks:
    def test_lista_todas_as_tarefas(self, service, mock_repo):
        mock_repo.get_all.return_value = [MagicMock(), MagicMock()]
        resultado = service.list_tasks()
        assert len(resultado) == 2
        mock_repo.get_all.assert_called_once_with(status=None)

    def test_filtra_tarefas_por_status(self, service, mock_repo):
        mock_repo.get_all.return_value = []
        service.list_tasks(status=True)
        mock_repo.get_all.assert_called_once_with(status=True)


class TestGetTask:
    def test_retorna_tarefa_existente(self, service, mock_repo):
        task_id = uuid4()
        mock_repo.get_by_id.return_value = MagicMock(id=task_id)
        resultado = service.get_task(task_id)
        assert resultado.id == task_id

    def test_levanta_404_para_tarefa_inexistente(self, service, mock_repo):
        mock_repo.get_by_id.return_value = None
        with pytest.raises(HTTPException) as exc_info:
            service.get_task(uuid4())
        assert exc_info.value.status_code == 404


class TestCreateTask:
    def test_cria_tarefa_com_dados_validos(self, service, mock_repo):
        payload = TaskCreate(title="Estudar FastAPI")
        mock_task = MagicMock()
        mock_repo.create.return_value = mock_task
        resultado = service.create_task(payload)
        mock_repo.create.assert_called_once_with(payload)
        assert resultado == mock_task


class TestCompleteTask:
    def test_marca_tarefa_como_concluida(self, service, mock_repo):
        task_id = uuid4()
        mock_task = MagicMock(id=task_id, status=False)
        mock_repo.get_by_id.return_value = mock_task
        mock_repo.update.return_value = MagicMock(status=True)
        resultado = service.complete_task(task_id)
        assert resultado.status is True

    def test_nao_conclui_tarefa_inexistente(self, service, mock_repo):
        mock_repo.get_by_id.return_value = None
        with pytest.raises(HTTPException) as exc_info:
            service.complete_task(uuid4())
        assert exc_info.value.status_code == 404


class TestDeleteTask:
    def test_remove_tarefa_existente(self, service, mock_repo):
        task_id = uuid4()
        mock_repo.get_by_id.return_value = MagicMock(id=task_id)
        service.delete_task(task_id)
        mock_repo.delete.assert_called_once()

    def test_nao_remove_tarefa_inexistente(self, service, mock_repo):
        mock_repo.get_by_id.return_value = None
        with pytest.raises(HTTPException) as exc_info:
            service.delete_task(uuid4())
        assert exc_info.value.status_code == 404
