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

RUN git config --global user.email "noreply@neurodata.io"; git config --global user.name "NeuroData"
RUN git clone https://github.com/neurodata/ndontology.git

WORKDIR /ndontology
ENV PYTHONPATH /ndontology
RUN pip3 install -r requirements.txt
WORKDIR /ndontology/arascripts
RUN python3 parse_ara.py
RUN nohup bash -c "/usr/bin/mongod --config /etc/mongod.conf 2>&1 &"; mongoimport --db atlases --collection ara --drop --file ./ara.mongo.ingest.json; python3 index_ara.py; python3 nametree_ara.py
WORKDIR WORKDIR /ndontology/whsscripts
RUN python3 parse_whs.py
RUN nohup bash -c "/usr/bin/mongod --config /etc/mongod.conf 2>&1 &"; mongoimport --db atlases --collection whs --drop --file ./whs.mongo.ingest.json; python3 index_whs.py; python3 nametree_whs.py

