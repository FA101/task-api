# Escopo e Backlog — Task API MVP

## Escopo do MVP

API RESTful para gerenciamento de tarefas com operações CRUD completas, filtragem por status e persistência em PostgreSQL.

## Backlog de Funcionalidades

### ✅ Entregues (v1.0.0)

| ID  | Funcionalidade                        | Prioridade |
|-----|---------------------------------------|------------|
| F01 | Criar tarefa (POST /tasks)            | Alta       |
| F02 | Listar tarefas (GET /tasks)           | Alta       |
| F03 | Buscar tarefa por ID (GET /tasks/:id) | Alta       |
| F04 | Atualizar tarefa (PUT /tasks/:id)     | Alta       |
| F05 | Excluir tarefa (DELETE /tasks/:id)    | Alta       |
| F06 | Marcar como concluída (PATCH)         | Alta       |
| F07 | Filtrar por status (?status=true)     | Média      |
| F08 | Validação Pydantic                    | Alta       |
| F09 | Documentação Swagger automática       | Alta       |
| F10 | Testes unitários com Pytest           | Alta       |

### 🔜 Backlog Futuro (fora do MVP)

| ID  | Funcionalidade                        | Prioridade |
|-----|---------------------------------------|------------|
| F11 | Autenticação JWT                      | Alta       |
| F12 | Paginação nos resultados              | Média      |
| F13 | Migração com Alembic                  | Média      |
| F14 | Frontend React completo               | Baixa      |
| F15 | Deploy em container Docker            | Média      |
