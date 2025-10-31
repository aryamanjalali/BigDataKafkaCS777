from kafka import KafkaConsumer
import json

topic_name = 'weather-data'  # Kafka topic for streaming sensor readings

# Initialize Kafka consumer for weather sensor data
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],          # Kafka broker address
    auto_offset_reset='earliest',                  # Read messages from the beginning of the topic
    enable_auto_commit=True,                       # Commit offsets automatically
    group_id='weather-group',                      # Consumer group ID for this listener
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Decode JSON messages
)

print("📡 Kafka Consumer started... listening for messages\n")

# Continuously consume messages and process them
for message in consumer:
    data = message.value                           # Extract message payload
    temp = data['temperature']
    humidity = data['humidity']

    # Print out the received sensor data
    print(f"Sensor {data['sensor_id']} | Temp: {temp}°C | Humidity: {humidity}% | {data['timestamp']}")

    # Trigger alert if temperature crosses threshold
    if temp > 30:
        print(f"⚠️ ALERT: High temperature detected ({temp}°C)!\n")
