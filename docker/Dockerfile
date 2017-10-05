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

RUN git config --global user.email "noreply@neurodata.io"; git config --global user.name "NeuroData"
RUN git clone https://github.com/neurodata/ndontology.git

ENV PYTHONPATH /ndontology
RUN pip3 install -r /ndontology/requirements.txt

COPY entrypoint.sh /usr/local/bin/ndontology-entrypoint.sh
RUN chmod u+x /usr/local/bin/ndontology-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/ndontology-entrypoint.sh"]
