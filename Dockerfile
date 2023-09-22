FROM python:3.8 as base

WORKDIR /app

COPY . .
RUN chmod +x /app/setup.sh
RUN  /app/setup.sh
CMD sh -c "while sleep 1000; do :; done"