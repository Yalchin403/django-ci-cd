FROM python:3.9.5-slim
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install python3-dev default-libmysqlclient-dev build-essential libssl-dev
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
RUN python manage.py migrate