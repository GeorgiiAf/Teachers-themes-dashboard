FROM python:3.11

WORKDIR /app
ADD . /app

RUN apt update && apt install -y gcc

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
