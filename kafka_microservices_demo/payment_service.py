from kafka import KafkaConsumer, KafkaProducer
import json
import time
import random

# Create a consumer to listen to the 'order_topic'
consumer = KafkaConsumer(
    'order_topic',
    bootstrap_servers=['localhost:9092'],          # Kafka broker address
    auto_offset_reset='earliest',                  # Read from earliest available message
    enable_auto_commit=True,                       # Commit offsets automatically
    group_id='payment-group',                      # Consumer group for payment service
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Decode JSON messages
)

# Create a producer to publish to the 'payment_topic'
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],          # Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')    # Serialize messages as JSON
)

print("💳 Payment Service started. Listening for new orders...")

# Continuously consume order messages and simulate payments
for message in consumer:
    order = message.value                          # Extract order data
    print(f"🧾 Received Order: {order}")

    # Simulate processing time for payment
    time.sleep(2)

    # Randomly determine if payment succeeds or fails
    payment = {
        "order_id": order["order_id"],
        "user_id": order["user_id"],
        "amount": order["amount"],
        "status": random.choice(["payment_successful", "payment_failed"])
    }

    # Publish payment result event to Kafka
    producer.send('payment_topic', value=payment)
    print(f"✅ Payment Event Sent: {payment}\n")
