METCS777 Term Paper – Event-Driven Microservices using Kafka
Authors: Aryaman Jalali, Aditya Kocherlakota
Course: MET CS 777 – Big Data Analytics (Fall 2025)

Overview:
This demo implements an Event-Driven Microservices Architecture (EDA) using Apache Kafka.
Three independent services communicate asynchronously through Kafka topics, simulating an Amazon-like order lifecycle:
Order Placed → Payment Processed → Customer Notified.
Each service publishes or consumes messages without knowing the others, showing Kafka’s ability to decouple systems.

Environment Setup:

Ensure Docker Desktop is running.

Start Kafka and Zookeeper:
docker compose up -d

Install dependencies:
pip install -r requirements.txt

Components:

order_service.py – Publishes order_created events to Kafka (order_topic).

payment_service.py – Consumes order_topic, processes payments, and publishes payment_topic events.

notification_service.py – Consumes payment_topic and simulates sending user notifications.

docker-compose.yml – Kafka + Zookeeper setup.

requirements.txt – Python dependencies.

How to Run the Services:
Open three VS Code terminals:
Terminal 1 → python order_service.py
Terminal 2 → python payment_service.py
Terminal 3 → python notification_service.py

Data Flow:
[Order Service] → (order_topic) → [Payment Service] → (payment_topic) → [Notification Service]

Results Example:
Order Service:
📦 Order Created: {'order_id': 1001, 'user_id': 18, 'amount': 120.5, 'status': 'created'}
Payment Service:
🧾 Received Order ...
✅ Payment Event Sent: {'order_id': 1001, 'user_id': 18, 'amount': 120.5, 'status': 'payment_successful'}
Notification Service:
✅ Payment Successful for Order 1001 (User 18)
📨 Email sent to customer confirming successful order.

Explanation:
This demo shows Kafka’s publish-subscribe model for decoupled microservices.
Each service reacts to events rather than API calls, enabling asynchronous communication and scalability.
In production, these services could scale horizontally or run across containers.

Key Takeaways:

Kafka enables loose coupling between services.

Each service focuses on its own domain logic (orders, payments, notifications).

Architecture supports fault tolerance and horizontal scalability.