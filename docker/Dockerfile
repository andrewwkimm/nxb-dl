FROM ubuntu:latest

RUN \
    apt update && \
    apt install -y python3-pip

WORKDIR /nxb-dl

COPY dist/nxbdl-0.1.0-py3-none-any.whl .

RUN pip install nxbdl-0.1.0-py3-none-any.whl

CMD nxb-dl --help