FROM python:3.12-slim
RUN groupadd -r groupdjango && useradd -r -g groupdjango userdj

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /app/www/drfsite

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER userdj
