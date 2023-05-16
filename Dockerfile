FROM python:3.9-alpine3.13
LABEL maintainer="site.com"

ENV PYTHONUNDUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -n venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \ 
        django-user

ENV PATH="/py/bin:SPATH"

USER django-user