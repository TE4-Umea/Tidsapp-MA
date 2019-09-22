FROM python:3.7-slim

ADD ./app/requirements.txt /app/requirements.txt
# COPY ./docker-entrypoint.sh /app/docker-entrypoint.sh
ADD ./docker-entrypoint.sh /usr/local/bin/
# COPY ./app/.env.example /app/.env


WORKDIR /app

RUN apt-get clean \
    && apt-get -y update \
    && pip install --upgrade pip  \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

ADD ./app /app


# RUN chmod +x /usr/local/bin/docker-entrypoint.sh
# RUN sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]
# ENTRYPOINT sh /usr/local/bin/docker-entrypoint.sh
CMD ["uwsgi", "--ini", "uwsgi.ini"]