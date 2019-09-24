FROM python:3.7-slim


ADD ./app/requirements.txt /app/requirements.txt
ADD ./docker-entrypoint.sh /usr/local/bin/

WORKDIR /app

RUN apt-get clean \
    && apt-get -y update \
    && pip install --upgrade pip  \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

ADD ./app /app

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]