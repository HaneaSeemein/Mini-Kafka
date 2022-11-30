FROM ubuntu:latest

WORKDIR /usr/app/src
RUN apt update
RUN apt install python3 -y

COPY ./zookeeper.py ./
EXPOSE 9997/udp

CMD ["python3","./zookeeper.py"]
