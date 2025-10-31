METCS777 Term Paper – Real-Time Data Pipeline with Kafka
Authors: Aryaman Jalali, Aditya Kocherlakota
Course: MET CS 777 – Big Data Analytics (Fall 2025)

Overview:
This demo builds a real-time data pipeline using Apache Kafka to simulate IoT weather sensor data streaming continuously.
The producer sends temperature and humidity readings into Kafka, and the consumer processes them in real time.
A Streamlit dashboard visualizes the live data feed.

Environment Setup:

Install Docker Desktop and ensure it is running.

Open this folder in VS Code.

Start Kafka and Zookeeper:
docker compose up -d

Install Python dependencies:
pip install -r requirements.txt

Components:

producer.py – Simulates continuous weather sensor data and publishes to Kafka.

consumer.py – Consumes data and prints alerts when temperature > 30°C.

dashboard.py – Streamlit dashboard for live charts and alerts.

docker-compose.yml – Runs local Kafka + Zookeeper.

requirements.txt – Python dependencies.

How to Run:

Start Kafka → docker compose up -d

Run producer → python producer.py

Run consumer → python consumer.py

Run dashboard → streamlit run dashboard.py
Opens in browser

Results:

Continuous streaming of IoT sensor data through Kafka topics.

Real-time alerts for high temperatures shown in console.

Dynamic dashboard with live-updating temperature/humidity charts.

Summary statistics (average temperature, humidity, total messages).

Explanation:
This demo demonstrates Kafka as a real-time message broker connecting producers and consumers.
Producer → Kafka Broker → Consumer/Dashboard
It mimics cloud streaming systems such as AWS MSK or Confluent Cloud.

Example Output:
Produced: {'sensor_id': 124, 'temperature': 35.37, 'humidity': 48.39, 'timestamp': '2025-10-22 18:19:32'}
⚠️ ALERT: High temperature detected (35.37°C)!

Dashboard:
Real-time charts for temperature/humidity, live alerts, and summary stats at the bottom.
