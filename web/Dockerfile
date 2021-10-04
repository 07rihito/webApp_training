FROM ubuntu:latest

RUN mkdir /web
RUN mkdir /web/app
ARG app_dir=/web/app/
ADD ./requirements.txt /web
# ADD requirements.txt $app_dir
# WORKDIR $app_dir

RUN echo "now building ..."
RUN apt-get update
RUN apt-get install python3-pip -y \
    && apt-get install vim -y \
    && apt-get install curl -y \
    && apt-get clean all
#
RUN pip3 install --upgrade pip
RUN pip3 install -r /web/requirements.txt
# RUN pip3 install flask
# RUN pip3 install mysql-connector-python

RUN export set encoding=utf-8 >> ~/.vimrc
RUN export set fileencodings=iso-2022-jp,euc-jp,sjis,utf-8 >> ~/.vimrc
RUN export set fileformats=unix,dos,mac >> ~/.vimrc

