FROM python:3.6-slim

WORKDIR /app

ADD . /app

RUN set -ex \
    && apt-get update && apt-get install -y vim \
    && pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 9005 9001

CMD ["python", "app.py"]
