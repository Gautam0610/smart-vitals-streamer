from kafka import KafkaProducer
import os
import json

KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "vitals")

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_vitals(vitals):
    producer.send(KAFKA_TOPIC, vitals)
    producer.flush()

if __name__ == '__main__':
    # Example usage (replace with actual vitals data)
    sample_vitals = {"heart_rate": 75, "breaths_per_minute": 15}
    send_vitals(sample_vitals)
    print("Vitals sent to Kafka")