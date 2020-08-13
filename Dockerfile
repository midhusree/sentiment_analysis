# pull official base image
FROM python:3.8.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add make automake gcc g++ subversion python3-dev libffi-dev openssl-dev
# install dependencies
RUN pip install --upgrade pip

RUN export CFLAGS=-I/usr/include/libffi/include
RUN pip install pyOpenSSL
# copy project

RUN mkdir -p /home/app


# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/crawler

WORKDIR $APP_HOME
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN pip install -r requirements.txt
COPY . $APP_HOME


CMD ["python3", "main.py"]