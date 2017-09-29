from mongo:latest

RUN apt-get -y update
RUN apt-get -y upgrade 
RUN apt-get -y install \
    build-essential \
    gcc \
    git \   
    python3-dev \
    python3-pip \ 
    vim

# Modify child mongo to use /data/db2 as dbpath (because /data/db wont persist the build)
RUN mkdir -p /data/db2 \
    && echo "dbpath = /data/db2" > /etc/mongod.conf \
    && chown -R mongodb:mongodb /data/db2

RUN ls
RUN git config --global user.email "noreply@neurodata.io"; git config --global user.name "NeuroData"
RUN git clone https://github.com/neurodata/ndontology.git

ENV PYTHONPATH /ndontology
RUN pip3 install -r /ndontology/requirements.txt
