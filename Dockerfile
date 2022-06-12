FROM python:3.10-buster

COPY src /app
COPY pyproject.toml poetry.lock /app/

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="$PATH:/root/.local/bin"

RUN poetry install --no-dev

EXPOSE 8000

CMD poetry run uvicorn api.main:app --host 0.0.0.0 --reload
