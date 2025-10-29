# METCS777-term-paper-code-sample-1-Team1.py
# Kafka Producer - Simulates IoT weather data stream
# Run this file first

from kafka import KafkaProducer
import json
import random
import time

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'weather-data'

print("🚀 Kafka Producer started... streaming temperature & humidity data")

while True:
    data = {
        "sensor_id": random.randint(100, 999),
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send(topic_name, value=data)
    print(f"Produced: {data}")
    time.sleep(1)
