FROM python:latest

LABEL maintainer="ericghoubiguian@live.fr"

COPY . /opencv_webserver

WORKDIR /opencv_webserver

RUN apt upgrade -y

RUN apt update -y

RUN apt install python3-pip -y

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
