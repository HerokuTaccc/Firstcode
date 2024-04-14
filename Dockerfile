FROM nikolaik/python-nodejs:python3.10-nodejs19
RUN apt update && apt upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN apt-get -y install git
RUN apt-get install -y wget python3-pip curl bash neofetch ffmpeg software-properties-common
COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY . .
CMD python fban.py
