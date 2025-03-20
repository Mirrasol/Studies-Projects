dev:
	uv run python manage.py runserver

start:
	puv run python -m gunicorn _.asgi:application -k uvicorn.workers.UvicornWorker

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

lint:
	uv run flake8 _