help:
	cat Makefile

################################################################################

setup:
	pre-commit install --install-hooks
	poetry install

build:
	poetry install
	poetry run black src tests
	poetry run flake8 src tests
	poetry run mypy src tests --ignore-missing-import
	poetry run pytest --cov

lint:
	poetry run flake8 src tests

test:
	poetry run pytest -x --cov

type_check:
	poetry run mypy src tests --ignore-missing-import

################################################################################

.PHONY: \
	build \
	help \
	lint \
	setup \
	test \
	type_check
