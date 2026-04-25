# Task API

API RESTful para gerenciamento de tarefas desenvolvida com FastAPI, SQLAlchemy e PostgreSQL como projeto MVP de aprendizado em Inteligência Artificial Generativa aplicada à Engenharia de Software.

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://postgresql.org)
[![Licença: MIT](https://img.shields.io/badge/Licença-MIT-yellow)](./LICENSE)

---

## Descrição

API RESTful que permite criar, ler, atualizar e excluir tarefas (CRUD completo), com funcionalidade de marcar tarefas como concluídas e filtrar por status. Desenvolvida com arquitetura em camadas (Controller → Service → Repository → Database), seguindo os princípios SOLID, DRY e Clean Code.

---

## Tecnologias

| Camada        | Tecnologia                          |
|---------------|-------------------------------------|
| Framework     | FastAPI 0.115                       |
| Validação     | Pydantic v2                         |
| ORM           | SQLAlchemy 2.0                      |
| Banco de dados| PostgreSQL 16 + psycopg2            |
| Servidor      | Uvicorn                             |
| Testes        | Pytest + pytest-asyncio             |
| Formatação    | Black                               |
| Ambiente      | Python 3.12 + pipenv/Poetry         |

---

## Instalação e Setup

### Pré-requisitos

- Python 3.12+
- PostgreSQL instalado e em execução
- Git

### Passos

**1. Clone o repositório**

```bash
git clone https://github.com/SEU_USUARIO/task-api.git
cd task-api
```

**2. Configure as variáveis de ambiente**

```bash
cp .env-example .env
# Edite o .env com suas credenciais do PostgreSQL
```

**3. Crie o banco de dados**

```sql
-- No psql ou pgAdmin:
CREATE DATABASE taskdb;
```

**4. Instale as dependências**

```bash
make install
```

**5. Execute as migrações (criação das tabelas)**

```bash
make migrate
```

---

## Execução e Operação

### Iniciar o servidor

```bash
make run
```

A API estará disponível em:

- API: `http://localhost:8000`
- Swagger (docs): `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Health check: `http://localhost:8000/health`

### Executar testes

```bash
make test
```

### Formatar o código

```bash
make format
```

---

## Endpoints

| Método   | Endpoint               | Descrição                         |
|----------|------------------------|-----------------------------------|
| `GET`    | `/tasks`               | Listar todas as tarefas           |
| `GET`    | `/tasks?status=true`   | Filtrar tarefas concluídas        |
| `GET`    | `/tasks?status=false`  | Filtrar tarefas pendentes         |
| `POST`   | `/tasks`               | Criar nova tarefa                 |
| `GET`    | `/tasks/{id}`          | Buscar tarefa por UUID            |
| `PUT`    | `/tasks/{id}`          | Atualizar tarefa                  |
| `PATCH`  | `/tasks/{id}/complete` | Marcar tarefa como concluída      |
| `DELETE` | `/tasks/{id}`          | Excluir tarefa                    |
| `GET`    | `/health`              | Smoke test / health check         |

### Exemplos de requisição (curl)

**Criar tarefa**

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar FastAPI", "description": "Capítulos 3 e 4"}'
```

**Listar todas as tarefas**

```bash
curl http://localhost:8000/tasks
```

**Filtrar tarefas concluídas**

```bash
curl "http://localhost:8000/tasks?status=true"
```

**Buscar tarefa por ID**

```bash
curl http://localhost:8000/tasks/123e4567-e89b-12d3-a456-426614174000
```

**Atualizar tarefa**

```bash
curl -X PUT http://localhost:8000/tasks/123e4567-e89b-12d3-a456-426614174000 \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar FastAPI — avançado", "status": false}'
```

**Marcar como concluída**

```bash
curl -X PATCH http://localhost:8000/tasks/123e4567-e89b-12d3-a456-426614174000/complete
```

**Excluir tarefa**

```bash
curl -X DELETE http://localhost:8000/tasks/123e4567-e89b-12d3-a456-426614174000
```

---

## Como a IA acelerou este projeto

### GitHub Copilot

O GitHub Copilot foi utilizado como par de programação ao longo de todo o desenvolvimento:

- **Geração de boilerplate**: a estrutura de arquivos `__init__.py`, imports e decoradores FastAPI foram gerados em segundos, economizando aproximadamente 40 minutos de digitação mecânica.
- **Autocompletar inteligente**: ao digitar o nome de um método no `TaskService`, o Copilot sugeriu a implementação completa com tratamento de erros, reduzindo o tempo de codificação em cerca de 60%.
- **Refatorações multiarquivo**: com o Copilot Chat, foi possível solicitar a refatoração do padrão Repository em todos os arquivos simultaneamente.
- **Geração de testes unitários**: os testes para `TestListTasks`, `TestGetTask` e `TestCompleteTask` foram gerados via prompt no Copilot Chat e ajustados manualmente, economizando cerca de 30 minutos.

### Claude (Anthropic)

Utilizado para decisões arquiteturais, prompt engineering e geração de documentação estruturada:

- Geração do `README.md` completo com todas as seções exigidas.
- Validação das escolhas de design patterns (Repository, Service Layer, Dependency Injection).
- Aplicação do modelo CO-STAR para prompts mais precisos e econômicos em tokens.

### Importância da revisão humana

Toda saída gerada por IA foi revisada antes de ser incorporada ao projeto. Pontos críticos incluíram:

- Verificação de que os mocks nos testes unitários refletiam o comportamento real do repositório.
- Ajuste de nomes de variáveis para seguir a nomenclatura semântica em português.
- Confirmação de que as configurações CORS estavam restritas à origem correta.

A IA acelera a implementação, mas a responsabilidade pela qualidade, segurança e coerência arquitetural permanece com o desenvolvedor.

---

## Arquitetura

```
Cliente (React / curl)
    ↓ HTTP/JSON
Controller  (app/controllers/task_controller.py)
    ↓ chama
Service     (app/services/task_service.py)
    ↓ acessa
Repository  (app/repositories/task_repository.py)
    ↓ SQL
PostgreSQL  (banco de dados local)
```

Diagrama completo disponível em `docs/architecture.mmd`.

---

## Segurança

- Variáveis de ambiente isoladas em `.env` (fora do controle de versão).
- Validação de entrada em todos os endpoints via Pydantic.
- CORS restrito à origem `http://localhost:3000`.
- Sem credenciais hardcoded no código.
- Práticas baseadas em OWASP Top 10 e NIST Cybersecurity Framework.

> **Limitação de IA**: nenhuma chave de API ou senha foi enviada a serviços externos. Os dados de desenvolvimento existem apenas localmente. O Claude (claude.ai) não armazena dados de sessão entre conversas.

---

## Instruções de Upgrade e Migração

### Migração para Node.js (futuro)

Caso o projeto evolua para uma stack com Node.js:

1. Instale o Node.js LTS: `nvm install --lts`
2. Substitua FastAPI por Express.js ou NestJS.
3. Substitua SQLAlchemy por Prisma ORM (já listado na stack tecnológica).
4. Substitua Pydantic por Zod para validação de schemas no TypeScript.
5. Mantenha a estrutura em camadas (Controller → Service → Repository).
6. Os endpoints e contratos JSON permanecem compatíveis — apenas a implementação muda.

### Migração para Alembic (versionamento de banco de dados)

```bash
pip install alembic
alembic init alembic
# Configure alembic.ini com a DATABASE_URL
alembic revision --autogenerate -m "feat: cria tabela tasks"
alembic upgrade head
```

---

## Limitações

- Sem autenticação/autorização (JWT não implementado no MVP).
- Sem paginação nos resultados de listagem.
- Migrações criadas automaticamente via `create_all` (não recomendado para produção — usar Alembic).
- Sem containerização (Docker fora do escopo do MVP).
- Sem CI/CD automatizado.

---

## Troubleshooting

**Erro: `could not connect to server`**
Verifique se o PostgreSQL está em execução: `sudo service postgresql start` (Linux) ou via pgAdmin (Windows/macOS).

**Erro: `database "taskdb" does not exist`**
Crie o banco manualmente: `createdb taskdb` ou via psql: `CREATE DATABASE taskdb;`

**Erro: `ModuleNotFoundError`**
Execute `make install` para instalar as dependências.

**Porta 8000 ocupada**
Use `lsof -i :8000` para identificar o processo e encerrá-lo, ou altere a porta em `make run`.**Erro: UnicodeDecodeError ao conectar no PostgreSQL (Windows)**
Ocorre quando o PostgreSQL retorna mensagens de erro em português. 
Já corrigido em `app/core/config.py` com `LANG=en_US.UTF-8`.
Certifique-se de usar Python 3.12 — o Python 3.14 é incompatível 
com psycopg2-binary e pydantic-core.

---

## Checklist de Submissão

- [x] Repositório GitHub público e acessível
- [x] Todos os arquivos solicitados presentes
- [x] README.md completo com todas as seções exigidas
- [x] Histórico de commits com padrão Conventional Commits
- [x] `requirements.txt` com dependências e versões
- [x] Testes unitários com instruções de execução
- [x] Variáveis de ambiente em `.env` (excluído via `.gitignore`)
- [x] Branch `main` limpo
- [x] Release v1.0.0 com CHANGELOG
- [x] Licença MIT presente
- [x] Diagrama de arquitetura em `.mmd`
- [x] Documentação de escopo em `/docs`
- [x] Todos os textos em português (Brasil)
- [x] Instruções de upgrade/migração incluídas
- [x] Smoke test via `/health` documentado

---

## Licença

Distribuído sob a licença [MIT](./LICENSE).
