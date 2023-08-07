FROM python:3.8.13-alpine3.16

COPY requirements.txt /
COPY lib/requirements.txt /lib/requirements.txt
RUN pip --no-cache-dir install --upgrade pip setuptools
RUN pip --no-cache-dir install -r /lib/requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
RUN pip --no-cache-dir install "Flask[async]"

# COPY conf/supervisor/ /etc/supervisor.d/
COPY . /webapps
WORKDIR /webapps
