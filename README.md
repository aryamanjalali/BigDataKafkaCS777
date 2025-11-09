# Apache Kafka: Real-Time Data Pipelines & Event-Driven Microservices

A comprehensive implementation demonstrating Kafka-based real-time data pipelines and microservice-driven event communication. This project showcases two distinct use cases: real-time IoT data streaming and event-driven microservices architecture.

## Overview

This repository contains the complete implementation for the Big Data Analytics (CS777) Term Paper project. It demonstrates advanced Kafka concepts including real-time data streaming, event-driven microservices, and scalable data pipeline architectures.

## Features

- **Real-Time Data Streaming**: IoT sensor data streaming with live visualization
- **Event-Driven Microservices**: Independent microservices communicating via Kafka
- **Dockerized Setup**: Complete Docker Compose configurations for easy deployment
- **Interactive Dashboards**: Streamlit-based real-time monitoring
- **Scalable Architecture**: Designed for production-ready implementations

## Project Structure

The repository is divided into two main components:

### 1. Kafka Realtime Demo (`Kafka_realtime_demo/`)

A real-time data streaming pipeline that simulates IoT weather sensor data.

**Components:**
- **Producer**: Streams live temperature and humidity data to Kafka topics
- **Consumer**: Processes and logs data from Kafka
- **Dashboard**: Interactive Streamlit app for real-time monitoring
- **Docker Setup**: Includes `docker-compose.yml` to spin up Kafka and Zookeeper

**Features:**
- Real-time data ingestion
- Dynamic visualization
- Sub-second data processing
- AWS S3 integration for data storage

### 2. Kafka Microservices Demo (`kafka_microservices_demo/`)

A simulation of event-driven communication between independent microservices.

**Services:**
- **Order Service**: Publishes new orders to Kafka
- **Payment Service**: Processes payments and updates order status
- **Notification Service**: Sends alerts based on payment results

**Features:**
- Event-driven architecture
- Service decoupling
- Fault tolerance
- Scalable design

## Technologies Used

- **Apache Kafka**: Distributed streaming platform
- **Docker**: Containerization
- **Python 3.12**: Core programming language
- **Streamlit**: Real-time dashboard visualization
- **AWS EC2/S3**: Cloud infrastructure
- **Kafka-Python**: Python client for Kafka
- **Pandas**: Data manipulation
- **Matplotlib**: Data visualization

## Prerequisites

- macOS 14 (Apple Silicon) or Linux
- Docker Desktop v4.32+
- Python 3.12+
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aryamanjalali/BigDataKafkaCS777.git
cd BigDataKafkaCS777
```

2. Install Python dependencies:
```bash
pip install kafka-python streamlit pandas matplotlib docker
```

3. Ensure Docker Desktop is running

## Usage

### Kafka Realtime Demo

1. Navigate to the demo directory:
```bash
cd Kafka_realtime_demo
```

2. Start Kafka and Zookeeper:
```bash
docker-compose up -d
```

3. Run the producer (in a separate terminal):
```bash
python producer.py
```

4. Run the consumer (in another terminal):
```bash
python consumer.py
```

5. Launch the Streamlit dashboard:
```bash
streamlit run dashboard.py
```

### Kafka Microservices Demo

1. Navigate to the demo directory:
```bash
cd kafka_microservices_demo
```

2. Start Confluent Kafka:
```bash
docker-compose up -d
```

3. Run each service in separate terminals:
```bash
# Terminal 1: Order Service
python order_service.py

# Terminal 2: Payment Service
python payment_service.py

# Terminal 3: Notification Service
python notification_service.py
```

## Key Learning Objectives

- Understanding distributed message queues and event-driven systems
- Designing scalable real-time data pipelines
- Integrating Python with Kafka for streaming data analytics
- Visualizing live data updates in real time
- Implementing microservices architecture with event-driven communication

## Project Details

Each subproject contains its own detailed README.md with:
- Environment setup instructions
- Step-by-step execution guide
- Code snippets and explanations
- Dataset generation and sample data explanation

## Authors

- **Aryaman Jalali** - [GitHub](https://github.com/aryamanjalali) | [LinkedIn](https://www.linkedin.com/in/aryamanjalali/)
- **Aditya Kocherlakota**

## License

This project is for educational and research purposes.

## Acknowledgments

- Apache Kafka community
- Confluent for Kafka tooling
- Streamlit for visualization framework
