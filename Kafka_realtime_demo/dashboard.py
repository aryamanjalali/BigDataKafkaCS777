# METCS777-term-paper-code-sample-3-Team1.py
# Streamlit Dashboard for Kafka Real-Time Data Pipeline
# Author: Aryan Jalali, Aditya Kocherlakota

import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd
from datetime import datetime

# Page setup
st.set_page_config(page_title="Kafka Real-Time Dashboard", layout="wide")
st.title("🌡️ Real-Time Weather Sensor Dashboard")

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'weather-data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='streamlit-dashboard',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Data buffer
data = []

# Layout setup
alert_placeholder = st.empty()
table_placeholder = st.empty()
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📈 Temperature (°C)")
    chart_temp = st.empty()
with col2:
    st.markdown("### 💧 Humidity (%)")
    chart_humidity = st.empty()

footer_placeholder = st.empty()

# Live loop
for message in consumer:
    record = message.value
    record['timestamp'] = datetime.strptime(record['timestamp'], "%Y-%m-%d %H:%M:%S")
    data.append(record)

    # Keep last 50 messages
    df = pd.DataFrame(data[-50:])

    # Alert banner for high temperature
    latest_temp = df.iloc[-1]['temperature']
    if latest_temp > 30:
        alert_placeholder.warning(f"⚠️ ALERT: High temperature detected ({latest_temp}°C)!")
    else:
        alert_placeholder.info(f"✅ Normal temperature ({latest_temp}°C)")

    # Update charts
    chart_temp.line_chart(df, x='timestamp', y='temperature', use_container_width=True)
    chart_humidity.line_chart(df, x='timestamp', y='humidity', use_container_width=True)

    # Display recent data table
    table_placeholder.dataframe(df[::-1].head(10), use_container_width=True)

    # Footer summary (fills empty bottom area)
    avg_temp = df['temperature'].mean()
    avg_hum = df['humidity'].mean()
    total_msgs = len(data)
    footer_placeholder.markdown(
        f"""
        ---
        **📊 Summary (last {len(df)} messages)**  
        - Average Temperature: **{avg_temp:.2f}°C**  
        - Average Humidity: **{avg_hum:.2f}%**  
        - Total Messages Processed: **{total_msgs}**  
        """,
        unsafe_allow_html=True
    )
