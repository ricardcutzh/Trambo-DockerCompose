FROM nginx:alpine

WORKDIR /usr/share/nginx/html

RUN apk update \
    && apk add --no-cache bash git openssh

COPY ./static/css /usr/share/nginx/html

COPY ./static/js /usr/share/nginx/html
