FROM python:3.9.5-alpine3.13

# RUN apt-get update \
# && apt-get install gcc -y \
# && apt-get clean

# COPY requirements.txt /app/requirements.txt
# COPY . /app
# ENTRYPOINT uvicorn main:app --reload --host 0.0.0.0 --port 1234

COPY ./pub /app

WORKDIR /app

RUN pip install --user -r requirements.txt

WORKDIR /app
