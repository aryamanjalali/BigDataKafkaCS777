from kafka import KafkaProducer
import json
import time
import random

# Initialize Kafka producer to send JSON-encoded messages
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],                    # Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Serialize messages as JSON
)

topic_name = 'order_topic'                                   # Kafka topic for new orders

print("🛒 Order Service started. Generating new orders...")

order_ids = 1000
# Continuously create and publish new orders
while True:
    order = {
        "order_id": order_ids,                               # Unique order ID
        "user_id": random.randint(1, 100),                   # Random user ID
        "amount": round(random.uniform(10.0, 500.0), 2),     # Random order amount
        "status": "created"                                  # Initial order status
    }

    # Publish order event to Kafka topic
    producer.send(topic_name, value=order)
    print(f"📦 Order Created: {order}")

    order_ids += 1                                           # Increment order ID
    time.sleep(2)                                            # Wait before sending next order
