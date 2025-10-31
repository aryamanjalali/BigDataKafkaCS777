from kafka import KafkaConsumer
import json
import time

# Create a Kafka consumer subscribed to the 'payment_topic'
consumer = KafkaConsumer(
    'payment_topic',
    bootstrap_servers=['localhost:9092'],        # Kafka broker address
    auto_offset_reset='earliest',                # Start reading from the earliest message
    enable_auto_commit=True,                     # Commit message offsets automatically
    group_id='notification-group',               # Consumer group for notification service
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Decode JSON messages
)

print("📧 Notification Service started. Waiting for payment updates...\n")

# Continuously listen for messages on the topic
for message in consumer:
    payment = message.value                      # Extract payment event data
    status = payment["status"]                   # Read payment status field

    # Handle success and failure scenarios
    if status == "payment_successful":
        print(f"✅ Payment Successful for Order {payment['order_id']} (User {payment['user_id']})")
        print("📨 Email sent to customer confirming successful order.\n")
    else:
        print(f"❌ Payment Failed for Order {payment['order_id']} (User {payment['user_id']})")
        print("⚠️ Email sent to customer: payment failed. Please retry.\n")

    # Simulate delay between notifications
    time.sleep(1)
