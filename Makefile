.DEFAULT_GOAL := help

.PHONY: help lint format typecheck test check

help:  ## Показать команды
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

lint:  ## Ruff: проверка и формат
	uv run ruff check .
	uv run ruff format --check .

format:  ## Ruff: исправить код
	uv run ruff check --fix .
	uv run ruff format .

typecheck:  ## Mypy
	uv run mypy

test:  ## Pytest: unit
	uv run pytest

check: lint typecheck test  ## lint, typecheck и unit-тесты
