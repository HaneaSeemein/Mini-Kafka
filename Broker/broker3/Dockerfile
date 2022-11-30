FROM ubuntu:latest

WORKDIR /usr/app/src
RUN apt update
RUN apt install python3 -y

COPY ./broker3.py ./
EXPOSE 9996/udp

CMD ["python3","./broker3.py"]
