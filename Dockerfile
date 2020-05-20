#Definition of based image for the generation of Docker image
FROM python:latest

#Definition of maintainer (me)
LABEL maintainer="ericghoubiguian@live.fr"

#Copy all the files and directories in the newly created directory opencv_webserver
COPY . /opencv_webserver

#Change work directory for the opencv_webserver project one
WORKDIR /opencv_webserver

#
RUN apt upgrade -y && apt update -y

#Install the pip3 utilitary to manage and install python packages 
RUN apt install python3-pip -y

#Run the pip3 utilitary to install all python packages listed in the requirements.txt file
RUN pip3 install -r requirements.txt

#Expose the docker container listening port
EXPOSE 5000

#Container instruction as entrypoint: 'python3 app.py'
ENTRYPOINT ["python3", "app.py"]
