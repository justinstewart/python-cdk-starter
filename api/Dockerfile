FROM public.ecr.aws/lambda/python:3.10

RUN pip install -U pip poetry

WORKDIR ${LAMBDA_TASK_ROOT}

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --format=requirements.txt > requirements-poetry.txt
RUN pip install -r requirements-poetry.txt --target . --upgrade

COPY src src
