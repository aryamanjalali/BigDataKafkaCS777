# notification_service.py
# Consumes 'payment_processed' events and simulates sending user notifications
# Author: Aryan Jalali, Aditya Kocherlakota

from kafka import KafkaConsumer
import json
import time

# Initialize consumer for 'payment_topic'
consumer = KafkaConsumer(
    'payment_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='notification-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📧 Notification Service started. Waiting for payment updates...\n")

for message in consumer:
    payment = message.value
    status = payment["status"]

    if status == "payment_successful":
        print(f"✅ Payment Successful for Order {payment['order_id']} (User {payment['user_id']})")
        print("📨 Email sent to customer confirming successful order.\n")
    else:
        print(f"❌ Payment Failed for Order {payment['order_id']} (User {payment['user_id']})")
        print("⚠️ Email sent to customer: payment failed. Please retry.\n")

    # simulate slight delay
    time.sleep(1)
