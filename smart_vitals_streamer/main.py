import time
import os
from smart_vitals_streamer.vitals_generator import generate_vitals
from smart_vitals_streamer.kafka_producer import send_vitals
from smart_vitals_streamer.anomaly_generator import inject_anomalies


if __name__ == "__main__":
    while True:
        vitals = generate_vitals()
        vitals = inject_anomalies(vitals)
        send_vitals(vitals)
        print("Vitals sent: {}".format(vitals))
        time.sleep(1)  # Send vitals every 1 second