FROM python:3.9-slim-buster

WORKDIR /app

COPY smart_vitals_streamer /app/smart_vitals_streamer

RUN pip install --no-cache-dir kafka-python

ENV KAFKA_BROKER=localhost:9092
ENV KAFKA_TOPIC=vitals

CMD ["python", "smart_vitals_streamer/main.py"]