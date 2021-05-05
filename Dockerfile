FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 8000

COPY . /app