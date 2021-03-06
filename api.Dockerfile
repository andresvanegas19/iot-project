# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# ENV PYTHONPATH "${PYTHONPATH}:/"
# ENV PORT=8000


# RUN pip install --upgrade pip

# COPY ./requirements.txt /app/

# RUN pip install -r requirements.txt psycopg2-binary

# COPY ./app /app

# ENTRYPOINT python3 app/main.py

FROM python:latest

WORKDIR /code

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY ./app /code

# CMD ["python", "-u", "app.py"]
