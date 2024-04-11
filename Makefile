help:
	cat Makefile

################################################################################

setup:
	pre-commit install --install-hooks
	poetry install

build:
	poetry install
	make lint
	make reformat
	make type_check
	make test

lint:
	poetry run flake8 src tests

reformat:
	poetry run black src tests

make setup:
	pre-commit install --install-hooks
	poetry config installer.modern-installation false
	poetry install

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
