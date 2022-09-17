FROM ubuntu:22.04

COPY . /

RUN apt-get update \
      && apt-get -y install python3 python3-pip \
      && pip install -r /requirements.txt

ENTRYPOINT ["/logs-generator.py"]
