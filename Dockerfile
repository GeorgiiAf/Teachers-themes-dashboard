FROM python:3.11

WORKDIR /app

ADD . /app

RUN apt update && apt install -y \
    gcc \
    libpq-dev \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    rustc \
    cargo

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
