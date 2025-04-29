FROM python:3.12-slim

WORKDIR /opt

COPY ./requirements.txt /opt/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /opt/requirements.txt \
    && rm -rf /root/.cache/pip
