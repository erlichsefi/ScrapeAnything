FROM python:3.8 as base

WORKDIR /app

COPY . .
RUN ./setup.sh