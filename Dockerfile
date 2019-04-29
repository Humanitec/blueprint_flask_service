FROM python:3.6-alpine3.7

RUN apk update

WORKDIR /code

RUN apk add --no-cache postgresql-libs bash nginx
RUN apk add --no-cache --virtual .build-deps git python-dev gcc musl-dev postgresql-dev libffi-dev libressl-dev

COPY ./requirements/base.txt requirements/base.txt
COPY ./requirements/production.txt requirements/production.txt
RUN pip install --upgrade pip && pip install -r requirements/production.txt

ADD . /code

RUN apk del .build-deps

ENTRYPOINT ["bash", "/code/scripts/docker-entrypoint.sh"]