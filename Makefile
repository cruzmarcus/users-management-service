
poetry_install:
    curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="$PATH:/root/.local/bin" && \
    poetry config virtualenvs.in-project true && \
    poetry install



create-dev-env:
	make poetry_install && \
	poetry install 


create-prod-env:
	make poetry_install && \
	poetry install --no-dev


update-dev-dependencies:
	poetry shell && \
	poetry update


run-tests:
	poetry shell && pytest -sv


run-users-management-service::
	poetry shell && \
	docker-compose -f test/docker-compose.yml -d up


cleaup:
	docker-compose -f test/docker-compose.yml down
