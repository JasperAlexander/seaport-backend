# syntax=docker/dockerfile:1
FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN apt-get update

COPY . .

RUN python3.10 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3.10 manage.py makemigrations
RUN python3.10 manage.py migrate