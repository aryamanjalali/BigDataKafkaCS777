import streamlit as st
from kafka import KafkaConsumer
import json
import pandas as pd
from datetime import datetime

# Set up Streamlit page configuration
st.set_page_config(page_title="Kafka Real-Time Dashboard", layout="wide")
st.title("🌡️ Real-Time Weather Sensor Dashboard")

# Create Kafka consumer to read from 'weather-data' topic
consumer = KafkaConsumer(
    'weather-data',
    bootstrap_servers=['localhost:9092'],         # Kafka broker address
    auto_offset_reset='latest',                   # Read only new incoming data
    enable_auto_commit=True,                      # Commit message offsets automatically
    group_id='streamlit-dashboard',               # Consumer group ID for dashboard
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Decode messages from JSON
)

# Store streamed messages
data = []

# Build Streamlit layout placeholders
alert_placeholder = st.empty()                   # For alert messages
table_placeholder = st.empty()                   # For recent data table
col1, col2 = st.columns(2)                       # Split screen into two charts
with col1:
    st.markdown("### 📈 Temperature (°C)")
    chart_temp = st.empty()
with col2:
    st.markdown("### 💧 Humidity (%)")
    chart_humidity = st.empty()

footer_placeholder = st.empty()                  # For summary statistics

# Continuously consume Kafka messages and update dashboard
for message in consumer:
    record = message.value
    record['timestamp'] = datetime.strptime(record['timestamp'], "%Y-%m-%d %H:%M:%S")
    data.append(record)

    # Keep only the most recent 50 readings
    df = pd.DataFrame(data[-50:])

    # Display alert banner if latest temperature exceeds threshold
    latest_temp = df.iloc[-1]['temperature']
    if latest_temp > 30:
        alert_placeholder.warning(f"⚠️ ALERT: High temperature detected ({latest_temp}°C)!")
    else:
        alert_placeholder.info(f"✅ Normal temperature ({latest_temp}°C)")

    # Update temperature and humidity charts
    chart_temp.line_chart(df, x='timestamp', y='temperature', use_container_width=True)
    chart_humidity.line_chart(df, x='timestamp', y='humidity', use_container_width=True)

    # Show last 10 records in a live-updating table
    table_placeholder.dataframe(df[::-1].head(10), use_container_width=True)

    # Display summary stats at bottom of dashboard
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
