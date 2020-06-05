FROM python:3.6-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 9001

ENV NAME world

CMD ["python", "app.py"]
