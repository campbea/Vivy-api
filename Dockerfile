FROM python:3.5-onbuild

RUN mkdir /src
ADD . /src
WORKDIR /src
RUN pip install -r requirements.txt

WORKDIR /src/vivy
