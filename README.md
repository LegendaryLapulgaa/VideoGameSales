# 🎮 Video Game Sales Analysis and Prediction

This project analyzes and models global video game sales using the `vgsales.csv` dataset. It combines exploratory data analysis (EDA) with a machine learning regression model (Random Forest) to predict game sales based on features like platform, genre, and year.

---

## 📌 Project Overview

- **Dataset**: `vgsales.csv` (from [Kaggle](https://www.kaggle.com/datasets/gregorut/videogame-sales-with-ratings))
- **Goal**: 
  1. Analyze key trends in video game sales.
  2. Build a machine learning model to predict global sales.
  3. Deploy an interactive Streamlit app for real-time predictions.

---

## 🔍 Key Features

- Cleaned and explored data across multiple dimensions (platform, genre, year).
- Identified top-performing games and trends by region.
- Trained a Random Forest Regression model to predict sales.
- Deployed a Streamlit web app for user input and prediction.

---

## 🧪 Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core programming |
| Pandas | Data manipulation |
| Seaborn / Matplotlib | Data visualization |
| Scikit-learn | Machine learning modeling |
| Streamlit | Web app deployment |
| Joblib | Model serialization |

---

## 📊 Exploratory Data Analysis (EDA)

- 📈 Top 10 best-selling games globally
- 🧩 Global sales by genre and platform
- 🕹️ Platform performance over time
- 🌍 Regional preferences: NA, EU, JP, Other

---

## 🧠 Machine Learning Model

- **Model Used**: Random Forest Regressor
- **Target Variable**: `Global_Sales`
- **Features**:
  - Platform (encoded)
  - Genre (encoded)
  - Year of Release
  - Regional sales (optional)

### ✅ Performance Metrics:
- **R² Score**: ~0.65 *(example)*
- **RMSE**: ~0.85M units *(example)*

---

## 🚀 Streamlit Web App

The Streamlit app allows users to:
- Choose a platform, genre, and release year
- Get predicted global sales instantly

### ▶️ To Run Locally:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
