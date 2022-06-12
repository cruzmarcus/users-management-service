FROM python:3.10-buster

COPY src /app
COPY pyproject.toml /app

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD uvicorn api.main:app --reload
