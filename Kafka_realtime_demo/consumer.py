# METCS777-term-paper-code-sample-2-Team1.py
# Kafka Consumer - Reads and processes IoT data

from kafka import KafkaConsumer
import json

topic_name = 'weather-data'

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='weather-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📡 Kafka Consumer started... listening for messages\n")

for message in consumer:
    data = message.value
    temp = data['temperature']
    humidity = data['humidity']
    print(f"Sensor {data['sensor_id']} | Temp: {temp}°C | Humidity: {humidity}% | {data['timestamp']}")

    if temp > 30:
        print(f"⚠️ ALERT: High temperature detected ({temp}°C)!\n")
