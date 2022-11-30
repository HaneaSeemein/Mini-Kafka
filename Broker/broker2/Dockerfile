FROM ubuntu:latest

WORKDIR /usr/app/src
RUN apt update
RUN apt install python3 -y

COPY ./broker2.py ./
EXPOSE 9998/udp
CMD ["python3","./broker2.py"]
