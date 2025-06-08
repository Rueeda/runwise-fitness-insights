import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("🏃 Runwise Fitness Insights")

# Load data (adjust filename if needed)
df = pd.read_csv("fitness_data.csv")

# Sidebar filter
users = df['user_id'].unique()
selected_user = st.sidebar.selectbox("Select a user", users)

# Filter data
filtered_data = df[df['user_id'] == selected_user]

# Show summary stats
st.subheader(f"Workout Summary for User {selected_user}")
st.write(filtered_data.describe())

# Line chart of heart rate (if available)
if 'heart_rate' in df.columns:
    st.subheader("Heart Rate Over Time")
    st.line_chart(filtered_data['heart_rate'])
else:
    st.info("No heart rate data available.")

# Optional: Add more plots or stats below
