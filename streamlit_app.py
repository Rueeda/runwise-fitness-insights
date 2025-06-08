import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("runwise_simulated_data.csv")

# Show column names (for debugging or curiosity)
st.write("📌 Columns in your data:")
st.write(df.columns.tolist())

# App title
st.title("Runwise: Fitness Insights Dashboard")
st.markdown("📊 A 30-day analysis of Rueeda's simulated treadmill data.")

# Show Raw Data
st.subheader("Raw Data")
st.dataframe(df)

# Plot: Total Distance by Date
st.subheader("📈 Distance Over Time")
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Distance (km)'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Distance (km)")
ax.set_title("Daily Distance Covered")
plt.xticks(rotation=45)
st.pyplot(fig)

# Optional: Plot Running Speed
st.subheader("⚡ Running Speed Over Time")
fig2, ax2 = plt.subplots()
ax2.plot(df['Date'], df['Running Speed (km/h)'], color='green', marker='s')
ax2.set_xlabel("Date")
ax2.set_ylabel("Speed (km/h)")
ax2.set_title("Daily Speed")
plt.xticks(rotation=45)
st.pyplot(fig2)
