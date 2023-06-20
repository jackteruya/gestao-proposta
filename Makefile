.PHONY: install format lint test sec

install:
	@poetry install
format:
	@isort .
	@blue .
lint:
	@blue . --check
	@isort . --check
test:
	@pytest -v
sec:
	@pip-audit

create_super:
	python manage.py create_superadmin

docker:
    docker compose build
    docker compose up -b
