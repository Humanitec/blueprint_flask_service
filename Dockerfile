FROM python:3.7

WORKDIR /code

WORKDIR /code

COPY ./requirements/base.txt requirements/base.txt
COPY ./requirements/production.txt requirements/production.txt
RUN pip install --upgrade pip && pip install -r requirements/production.txt

ADD . /code

ENTRYPOINT ["bash", "/code/scripts/docker-entrypoint.sh"]