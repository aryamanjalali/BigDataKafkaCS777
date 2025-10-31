# BigDataKafkaCS777

This repository contains the complete implementation for our Big Data Analytics (CS777) Term Paper project, focused on demonstrating Kafka-based real-time data pipelines and microservice-driven event communication.

The repository is divided into two main components, each representing a unique Kafka use case:

Project Structure
1. Kafka Realtime Demo (Kafka_realtime_demo/)

A real-time data streaming pipeline that simulates IoT weather sensor data, publishes it to Kafka topics, and visualizes it dynamically using Streamlit dashboards.

Producer: Streams live temperature and humidity data

Consumer: Processes and logs data from Kafka

Dashboard: Interactive Streamlit app for real-time monitoring

Docker Setup: Includes docker-compose.yml to spin up Kafka and Zookeeper

README: Detailed setup, execution steps, and dataset explanation

2. Kafka Microservices Demo (kafka_microservices_demo/)

A simulation of event-driven communication between independent microservices using Kafka.

Order Service: Publishes new orders

Payment Service: Processes payments and updates order status

Notification Service: Sends alerts based on payment results

Docker Setup: Uses Confluent Kafka 7.6.1 for local message streaming

README: Step-by-step guide to setup, run, and visualize event flows

Environment Overview

macOS 14 (Apple Silicon)

Docker Desktop v4.32+

Python 3.12

Kafka-Python, Pandas, Streamlit, Matplotlib

Dockerized Confluent Kafka 7.6.1 setup for both demos

Key Learning Objectives

Understanding distributed message queues and event-driven systems

Designing scalable real-time data pipelines

Integrating Python with Kafka for streaming data analytics

Visualizing live data updates in real time

Authors

Aryaman Jalali

Aditya Kocherlakota

Note:

Each subproject has its own README.md containing:

Environment setup

How to run the code

Code snippets

Dataset generation and sample data explanation

You can explore either demo independently or run both to compare real-time streaming vs microservice-based event flow architectures.
