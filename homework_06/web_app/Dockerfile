FROM python:3.9-buster

WORKDIR /app

RUN pip install -U pip
RUN pip install -U setuptools wheel
RUN pip install poetry
RUN poetry config virtualenv.create false

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 5000

