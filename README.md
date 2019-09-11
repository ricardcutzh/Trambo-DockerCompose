# Intermediate Docker Exercice 5
## Exercise Description
The purpose of the following excercise is to learn how to use docker containers by using Dockerfiles and a docker-compose file to automate the deployment of the services that are part of the application
## How to Start:
* To run this excercise first you need docker and docker-compose installed
* To build all Dockerfiles run the following command:
```bash
$ docker-compose build
```
* To start all services in the docker-compose file just run:
```bash
$ docker-compose up
```
* To stop all services just run:
```bash
$ docker-compose down
```
## Architecture Diagram
The excercice requires four services:
* Redis: to store information
* Flask: Python framework for web applications
* Nginx Server: a server to serve static files (css, js)
* Nginx Proxy: a proxy server used to distribute requests

The following diagram shows how the whole application works:
