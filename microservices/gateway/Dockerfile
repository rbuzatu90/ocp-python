FROM python:3.10-slim-bullseye

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential vim netcat tcpdump strace curl procps\
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

ENV PYTHONUNBUFFERED=1
EXPOSE 8080

CMD ["python3", "app.py"]
