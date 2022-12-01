FROM ubuntu:latest

WORKDIR /usr/app/src
RUN apt update
RUN apt install python3 -y

COPY ./broker2.py ./
CMD ["python3","./broker2.py"]
