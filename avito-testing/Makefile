install:
	poetry install

dev:
	poetry run flask --app api/app.py --debug run

lint:
	poetry run ruff check api

fix:
	poetry run ruff check api --fix