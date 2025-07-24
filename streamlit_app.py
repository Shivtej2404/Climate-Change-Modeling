import streamlit as st
import numpy as np
import pickle

# Load trained model and scaler
model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Page setup
st.set_page_config(page_title="Climate Emission Predictor", layout="centered")
st.title("Climate Emission Predictor")
st.write("Enter basic climate values to predict CO₂ emissions.")

# --- Minimal Inputs ---
temperature = st.number_input("Temperature (°C)", value=15.0)
CO2_ppm = st.number_input("CO₂ Concentration (ppm)", value=410.0)
sea_level = st.number_input("Sea Level Deviation (mm)", value=0.0)

# Predict button
if st.button("🔍 Predict Emission"):
    # Fill other features with default/mid values
    year = 2023
    week_no = 26
    latitude = 0.0
    longitude = 0.0
    CO2_roll_mean = CO2_ppm
    sea_level_diff = 0.0
    temp_lag1 = temperature

    # Feature array
    features = np.array([[year, week_no, latitude, longitude, temperature,
                          CO2_ppm, sea_level, CO2_roll_mean,
                          sea_level_diff, temp_lag1]])
    
    # Scale and predict
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

    # Show result
    st.success(f"Estimated CO₂ Emission: **{prediction:.2f} units**")
