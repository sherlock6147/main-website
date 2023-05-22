FROM python:3.10-alpine3.16

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN apk add --upgrade --no-cache build-base linux-headers && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt

COPY app/ /app
WORKDIR /app

RUN adduser --disabled-password --no-create-home django

USER django

RUN mkdir -p /app/staticfiles

CMD ["python3", "manage.py", "collectstatic", "-y", "4", "--master", "--enable-threads", "--module", "website.wsgi"]

CMD ["uwsgi", "--socket", ":9000", "--workers", "4", "--master", "--enable-threads", "--module", "website.wsgi"]