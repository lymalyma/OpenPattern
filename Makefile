init:
	uv sync

dev:
	uv sync --extra dev

test:
	uv run pytest tests/

lint:
	uv run ruff check .

format:
	uv run ruff format .

# Legacy pip-based install (deprecated)
install-legacy:
	pip install -e .
