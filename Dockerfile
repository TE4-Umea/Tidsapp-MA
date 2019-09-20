FROM python:3.7-slim

COPY ./app/requirements.txt /app/requirements.txt
COPY ./app/.env.example /app/.env

WORKDIR /app

RUN apt-get clean \
    && apt-get -y update \
    && pip install --upgrade pip  \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

COPY ./app /app

CMD ["uwsgi", "--ini", "uwsgi.ini"]