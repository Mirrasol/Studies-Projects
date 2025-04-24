lint:
	uv run ruff check

flask-dev:
	uv run flask --app flask-practice/app.py --debug run

flask-lint:
	uv run ruff check flask-practice

avito-dev:
	uv run flask --app avito-testing/app.py --debug run

avito-lint:
	uv run ruff check avito-testing