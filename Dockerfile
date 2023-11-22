FROM python:3.10-slim-buster

ARG API_KEY

WORKDIR /app

ADD src .

RUN pip install -U pip \
    && pip install poetry \
    && poetry install

RUN \
    #Download movie data
    poetry run moviegpt data --start=2000 --end=2020 --path=/tmp --sample=0.02 \
    # Create VectorDB index
    && poetry run moviegpt index --api_key=$API_KEY

ENTRYPOINT ["bash", "-c", "poetry run moviegpt web"]
