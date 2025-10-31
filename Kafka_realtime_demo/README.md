MET CS 777 — Kafka Real-Time Data Streaming Demo  
Authors: Aryaman Jalali & Aditya Kocherlakota  

----------------------------------------------------------------------
ENVIRONMENT SETUP
----------------------------------------------------------------------

System Requirements:
- macOS 14+ (Apple Silicon) / Windows / Linux
- VS Code with integrated terminal
- Docker Desktop v4.32+
- Python 3.12+
- Streamlit for live dashboard visualization

Python Libraries:
pip install kafka-python streamlit pandas matplotlib

Docker Configuration:
This demo uses Confluent Kafka 7.6.1 and Zookeeper, configured via docker-compose.yml.

services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.6.1
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:7.6.1
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

Start the services:
docker compose up -d

Verify running containers:
docker ps

----------------------------------------------------------------------
HOW TO RUN THE CODE
----------------------------------------------------------------------

This demo simulates IoT weather sensors streaming temperature and humidity data into Kafka, visualized live through Streamlit.

Run each command in a separate terminal:

1. Start the Kafka Producer:
   python producer.py

2. Start the Kafka Consumer:
   python consumer.py

3. Launch the Streamlit Dashboard:
   streamlit run dashboard.py

Expected Output:
- Producer sends continuous temperature & humidity readings.
- Consumer receives the data and prints alerts for high temperature (>30°C).
- Dashboard updates live with temperature and humidity trends.

----------------------------------------------------------------------
CODE SNIPPETS
----------------------------------------------------------------------

Kafka Producer:
data = {
  "sensor_id": random.randint(100, 999),
  "temperature": round(random.uniform(20.0, 40.0), 2),
  "humidity": round(random.uniform(30.0, 80.0), 2),
  "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
}
producer.send('weather-data', value=data)

Streamlit Live Chart:
chart_temp.line_chart(df, x='timestamp', y='temperature')
chart_humidity.line_chart(df, x='timestamp', y='humidity')

Run dashboard → streamlit run dashboard.py
Opens in browser

----------------------------------------------------------------------
DATASET EXPLANATION
----------------------------------------------------------------------

Dataset Type:
Synthetic weather sensor data generated in real time — no external dataset required.

Generation Logic:
Each second, the producer script generates:
{
  "sensor_id": 312,
  "temperature": 29.85,
  "humidity": 53.22,
  "timestamp": "2025-10-30 19:22:15"
}

Fields:
- sensor_id: Random integer (100–999)
- temperature: Random float (20–40°C)
- humidity: Random float (30–80%)
- timestamp: Current system time

A sample parquet file (weather_sample.parquet) is included for reference.
Anyone can regenerate the dataset by running producer.py.

----------------------------------------------------------------------
SUMMARY
----------------------------------------------------------------------

<<<<<<< HEAD
Explanation:
This demo demonstrates Kafka as a real-time message broker connecting producers and consumers.
Producer → Kafka Broker → Consumer/Dashboard
It mimics cloud streaming systems such as AWS MSK or Confluent Cloud.

Example Output:
Produced: {'sensor_id': 124, 'temperature': 35.37, 'humidity': 48.39, 'timestamp': '2025-10-22 18:19:32'}
⚠️ ALERT: High temperature detected (35.37°C)!

Dashboard:
Real-time charts for temperature/humidity, live alerts, and summary stats at the bottom.
=======
This demo shows:
- Real-time IoT data streaming into Kafka
- Live visualization with Streamlit
- End-to-end local Kafka setup using Docker (Confluent 7.6.1)
>>>>>>> dff6077 (Code comments)
