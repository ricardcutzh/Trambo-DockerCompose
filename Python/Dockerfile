FROM ubuntu:18.04

RUN apt update \
    && apt install software-properties-common -y \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt install python3.7 -y

RUN apt install python3-pip -y

RUN pip3 install Flask

RUN pip3 install redis

WORKDIR /home

COPY . .

CMD python3 app.py
