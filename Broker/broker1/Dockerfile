FROM ubuntu:latest

WORKDIR /usr/app/src
RUN apt update
RUN apt install python3 -y

COPY ./broker1.py ./
EXPOSE 9997/udp
CMD ["python3","./broker1.py"]
