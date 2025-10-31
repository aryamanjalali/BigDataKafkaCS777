from kafka import KafkaProducer
import json
import random
import time

# Initialize Kafka producer to send JSON-encoded messages
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],                    # Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Serialize messages as JSON
)

topic_name = 'weather-data'                                  # Kafka topic for sensor data

print("🚀 Kafka Producer started... streaming temperature & humidity data")

# Continuously generate and publish random sensor readings
while True:
    data = {
        "sensor_id": random.randint(100, 999),               # Unique sensor identifier
        "temperature": round(random.uniform(20.0, 40.0), 2), # Random temperature value
        "humidity": round(random.uniform(30.0, 80.0), 2),    # Random humidity value
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")      # Current timestamp
    }

    # Publish the data record to the Kafka topic
    producer.send(topic_name, value=data)
    print(f"Produced: {data}")

    time.sleep(1)                                            # Wait 1 second before sending next reading
