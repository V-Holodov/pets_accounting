FROM python:3.8-slim-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install poetry==1.1.11
COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt --output requirements.txt

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt



FROM python:3.8-slim-buster

RUN mkdir -p /pets_app

WORKDIR /pets_app

RUN pip install --upgrade pip
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY . .

RUN mkdir -p vol/web/media && mkdir -p vol/web/static

RUN ["chmod", "+x", "/pets_app/entrypoint.sh"]
ENTRYPOINT ["/pets_app/entrypoint.sh"]
