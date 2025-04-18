lint:
	uv run ruff check

flask-dev:
	uv run flask --app flask-practice/app.py --debug run

flask-lint:
	uv run ruff check flask-practice