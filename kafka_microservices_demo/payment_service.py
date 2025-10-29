# payment_service.py
# Consumes 'order_created' events and publishes 'payment_processed' events
# Author: Aryaman Jalali, Aditya Kocherlakota

from kafka import KafkaConsumer, KafkaProducer
import json
import time
import random

# Initialize consumer for 'order_topic'
consumer = KafkaConsumer(
    'order_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='payment-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Initialize producer for 'payment_topic'
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("💳 Payment Service started. Listening for new orders...")

for message in consumer:
    order = message.value
    print(f"🧾 Received Order: {order}")

    # Simulate payment processing
    time.sleep(2)
    payment = {
        "order_id": order["order_id"],
        "user_id": order["user_id"],
        "amount": order["amount"],
        "status": random.choice(["payment_successful", "payment_failed"])
    }

    # Send payment result
    producer.send('payment_topic', value=payment)
    print(f"✅ Payment Event Sent: {payment}\n")
