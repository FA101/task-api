.PHONY: install run test format migrate

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	pytest tests/ -v --tb=short

format:
	black app/ tests/

migrate:
	python -c "from app.core.database import engine; from app.models.task import Base; Base.metadata.create_all(bind=engine); print('Tabelas criadas com sucesso.')"
