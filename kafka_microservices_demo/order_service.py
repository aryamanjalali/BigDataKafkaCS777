# order_service.py
# Publishes 'order_created' events to Kafka

from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'order_topic'

print("🛒 Order Service started. Generating new orders...")

order_ids = 1000
while True:
    order = {
        "order_id": order_ids,
        "user_id": random.randint(1, 100),
        "amount": round(random.uniform(10.0, 500.0), 2),
        "status": "created"
    }
    producer.send(topic_name, value=order)
    print(f"📦 Order Created: {order}")
    order_ids += 1
    time.sleep(2)
