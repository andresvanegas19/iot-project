# FROM python:3.7

# COPY . /app

# WORKDIR /app


# EXPOSE 80

# # CMD ["bash"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

EXPOSE 8000

COPY . /app