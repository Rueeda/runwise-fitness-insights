import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("runwise_simulated_data.csv")

# Header
st.title("🏃‍♀️ Runwise: Fitness Insights Dashboard")
st.markdown("#### A minimalist look at Rueeda’s running journey")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("📅 Total Days", len(df))
col2.metric("📏 Avg Distance", f"{df['Distance (km)'].mean():.2f} km")
col3.metric("⚡ Avg Speed", f"{df['Running Speed (km/h)'].mean():.1f} km/h")

st.markdown("---")

# Sidebar (no image)
st.sidebar.title("🧡 Your Motivation to Run")
st.sidebar.markdown("by Rueeda")
st.sidebar.markdown("Built with love & data 💻")

# Data table
st.subheader("📄 Raw Data")
st.dataframe(df)

# Distance plot
st.subheader("📈 Distance Over Time")
fig1, ax1 = plt.subplots()
ax1.plot(df['Date'], df['Distance (km)'], marker='o', color='#CC7351')
ax1.set_xlabel("Date")
ax1.set_ylabel("Distance (km)")
ax1.set_title("Daily Distance Covered")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Speed plot
st.subheader("⚡ Speed Over Time")
fig2, ax2 = plt.subplots()
ax2.plot(df['Date'], df['Running Speed (km/h)'], color='#A05C4E', marker='s')
ax2.set_xlabel("Date")
ax2.set_ylabel("Speed (km/h)")
ax2.set_title("Daily Running Speed")
plt.xticks(rotation=45)
st.pyplot(fig2)
