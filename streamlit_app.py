import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("runwise_simulated_data.csv")

# Streamlit App
st.title("Runwise: Fitness Insights Dashboard")
st.markdown("📊 A 30-day analysis of Rueeda's simulated treadmill data.")

# Show Data
st.subheader("Raw Data")
st.dataframe(df)

# Plotting total distance by day
st.subheader("📈 Total Distance by Day")
fig, ax = plt.subplots()
ax.plot(df['Day'], df['Distance (km)'], marker='o')
ax.set_xlabel("Day")
ax.set_ylabel("Distance (km)")
ax.set_title("Daily Distance")
st.pyplot(fig)

# Average speed or pace (optional)
if "Speed (km/h)" in df.columns:
    st.subheader("⚡ Average Speed Over Time")
    fig2, ax2 = plt.subplots()
    ax2.plot(df['Day'], df['Speed (km/h)'], color='green')
    ax2.set_xlabel("Day")
    ax2.set_ylabel("Speed (km/h)")
    st.pyplot(fig2)
