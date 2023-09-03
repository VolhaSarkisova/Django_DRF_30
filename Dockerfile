FROM python:3.10-alpine

WORKDIR /app

COPY . /app

ADD requirement.txt /app

RUN pip install -r requirement.txt

