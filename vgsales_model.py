import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("vgsales_model.pkl")

# Title
st.title("🎮 Video Game Sales Predictor")

# User Inputs for features model was trained on
year = st.number_input("Year of Release", min_value=1980, max_value=2025, value=2010)
na_sales = st.number_input("NA Sales (in millions)", min_value=0.0, value=1.0)
eu_sales = st.number_input("EU Sales (in millions)", min_value=0.0, value=1.0)
jp_sales = st.number_input("JP Sales (in millions)", min_value=0.0, value=0.5)
other_sales = st.number_input("Other Sales (in millions)", min_value=0.0, value=0.2)

# Create input dataframe
X_input = pd.DataFrame([{
    "Year": year,
    "NA_Sales": na_sales,
    "EU_Sales": eu_sales,
    "JP_Sales": jp_sales,
    "Other_Sales": other_sales
}])

# Predict
if st.button("Predict Sales"):
    prediction = model.predict(X_input)[0]
    st.success(f"📈 Predicted Global Sales: {prediction:.2f} million units")
