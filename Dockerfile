FROM python:3.10-alpine3.18

COPY . /book
RUN pip install -r /book/requirements.txt
WORKDIR /book
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password book-user
USER book-user
