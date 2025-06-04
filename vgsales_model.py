import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("vgsales_model.pkl")

# Title
st.title("🎮 Video Game Sales Predictor")

# User Inputs
platform = st.selectbox("Platform", ['Wii', 'NES', 'PS4', 'GB', 'DS'])  # Add more
genre = st.selectbox("Genre", ['Sports', 'Platform', 'Racing', 'Action'])  # Add more
year = st.number_input("Year of Release", min_value=1980, max_value=2025, value=2010)

# Encode Inputs (example — use one-hot or manual mapping as needed)
platform_map = {'Wii': 1, 'NES': 2, 'PS4': 3, 'GB': 4, 'DS': 5}
genre_map = {'Sports': 1, 'Platform': 2, 'Racing': 3, 'Action': 4}

X_input = pd.DataFrame([{
    "Platform": platform_map.get(platform, 0),
    "Genre": genre_map.get(genre, 0),
    "Year": year
}])

# Predict
if st.button("Predict Sales"):
    prediction = model.predict(X_input)[0]
    st.success(f"📈 Predicted Global Sales: {prediction:.2f} million units")
