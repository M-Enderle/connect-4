# syntax=docker/dockerfile:1
FROM python:3.8-alpine
RUN pip install --upgrade pip
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]