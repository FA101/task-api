#!/usr/bin/env bash
# Script de inicialização do repositório Git
# Execute: bash git-setup.sh
# Substitua <URL_DO_SEU_REPOSITORIO> pela URL real do GitHub

set -e

echo "=== Inicializando repositório Git ==="
git init

echo "=== Configurando .gitignore ==="
git add .gitignore
git commit -m "chore: adiciona .gitignore para Python, .env e dependências"

echo "=== Commit inicial — estrutura do projeto ==="
git add app/ docs/ tests/
git commit -m "feat: adiciona estrutura inicial do projeto em camadas"

echo "=== Commit — schemas Pydantic e modelos SQLAlchemy ==="
git add app/schemas/ app/models/ app/core/
git commit -m "feat: adiciona modelo Pydantic Task e modelo ORM SQLAlchemy"

echo "=== Commit — camadas Repository e Service ==="
git add app/repositories/ app/services/
git commit -m "feat: implementa Repository Pattern e Service layer para tarefas"

echo "=== Commit — Controller e ponto de entrada ==="
git add app/controllers/ app/main.py
git commit -m "feat: adiciona Controller FastAPI com endpoints CRUD para /tasks"

echo "=== Commit — testes unitários TDD ==="
git add tests/
git commit -m "test: adiciona testes unitários para TaskService com mocks (TDD)"

echo "=== Commit — dependências e configuração ==="
git add requirements.txt pyproject.toml Makefile
git commit -m "chore: adiciona requirements.txt, pyproject.toml e Makefile"

echo "=== Commit — variáveis de ambiente ==="
git add .env-example
git commit -m "chore: adiciona .env-example com modelo de variáveis de ambiente"

echo "=== Commit — documentação ==="
git add README.md CHANGELOG.md LICENSE docs/
git commit -m "docs: adiciona README.md completo, CHANGELOG e licença MIT"

echo "=== Tag de release v1.0.0 ==="
git tag -a v1.0.0 -m "v1.0.0 — MVP Task API com CRUD, testes e documentação"

echo ""
echo "=== Conectar ao repositório remoto ==="
echo "Execute os comandos abaixo substituindo pela URL do seu repositório:"
echo ""
echo "  git remote add origin <URL_DO_SEU_REPOSITORIO>"
echo "  git branch -M main"
echo "  git push -u origin main"
echo "  git push origin main --tags"
echo ""
echo "=== Concluído ==="
