# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [1.0.0] - 2026-04-25

### Adicionado
- API RESTful completa para gerenciamento de tarefas
- Endpoints: GET, POST, PUT, DELETE e PATCH `/tasks`
- Filtro por status via query parameter `?status=true|false`
- Modelo Pydantic com validação forte (title 3–100 chars, UUID, datetime UTC)
- Arquitetura em camadas: Controller → Service → Repository → PostgreSQL
- Persistência com SQLAlchemy e PostgreSQL via psycopg2
- Documentação automática via Swagger (`/docs`) e ReDoc (`/redoc`)
- Testes unitários com Pytest (cobertura do Service layer)
- Configuração via variáveis de ambiente com `.env` e `.env-example`
- Makefile com comandos `install`, `run`, `test`, `format`, `migrate`
- Diagrama de arquitetura em `.mmd` (Mermaid)

### Segurança
- Variáveis sensíveis isoladas em `.env` (excluído do Git via `.gitignore`)
- CORS configurado apenas para origens permitidas
- Validação de entrada via Pydantic em todos os endpoints

### Limitações conhecidas
- Sem autenticação/autorização (JWT não implementado no MVP)
- Sem paginação nos resultados de listagem
- Migrações manuais (Alembic não configurado)
- Banco de dados local (sem containerização)

---

## Como interpretar este arquivo

- `Adicionado` — novas funcionalidades
- `Alterado` — mudanças em funcionalidades existentes
- `Descontinuado` — funcionalidades que serão removidas em breve
- `Removido` — funcionalidades removidas nesta versão
- `Corrigido` — correção de bugs
- `Segurança` — vulnerabilidades corrigidas
