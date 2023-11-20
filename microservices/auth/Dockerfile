FROM registry.redhat.io/ubi9/python-39:latest

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

CMD ["python3", "app.py"]
