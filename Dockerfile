FROM ubuntu:16.04

MAINTAINER Paula de la Hoz <inversealien@protonmail.com>

RUN apt-get update
RUN apt-get install -y python python-pip git
RUN git clone https://github.com/terceranexus6/copylazyjacker proyecto
RUN pip install -r proyecto/requirements.txt
EXPOSE 8000
WORKDIR proyecto
CMD gunicorn app:app --log-file=- - --bind 0.0.0.0:8000
