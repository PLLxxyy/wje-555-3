FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends default-libmysqlclient-dev build-essential curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 38305
CMD ["sh", "-c", "python manage.py migrate && python manage.py seed_demo && python manage.py runserver 0.0.0.0:${DJANGO_PORT:-38305}"]

