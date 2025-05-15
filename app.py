import streamlit as st
import joblib
import pandas as pd

# Load saved model
model = joblib.load('car_price_model.pkl')

st.title("🚗 Car Price Prediction App")

st.markdown("Enter the car details below to get an estimated price:")

# Input fields
year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
odometer = st.number_input("Odometer (miles)", min_value=0, max_value=300000, value=60000)
manufacturer = st.selectbox("Manufacturer", ['ford', 'chevrolet', 'toyota', 'honda', 'nissan', 'jeep', 'other'])
fuel = st.selectbox("Fuel Type", ['gas', 'diesel', 'electric', 'hybrid', 'other'])
transmission = st.selectbox("Transmission", ['automatic', 'manual', 'other'])
drive = st.selectbox("Drive Type", ['fwd', 'rwd', '4wd'])
car_type = st.selectbox("Car Type", ['sedan', 'SUV', 'truck', 'hatchback', 'wagon', 'convertible', 'coupe', 'van', 'other'])
paint_color = st.selectbox("Paint Color", ['black', 'white', 'silver', 'blue', 'red', 'grey', 'green', 'custom', 'other'])
condition = st.selectbox("Condition", ['excellent', 'good', 'fair', 'like new', 'new', 'salvage'])
cylinders = st.selectbox("Cylinders", ['4 cylinders', '6 cylinders', '8 cylinders', '3 cylinders', '5 cylinders', '10 cylinders', '12 cylinders', 'other'])

# Convert to DataFrame
input_data = pd.DataFrame({
    'year': [year],
    'odometer': [odometer],
    'manufacturer': [manufacturer],
    'fuel': [fuel],
    'transmission': [transmission],
    'drive': [drive],
    'type': [car_type],
    'paint_color': [paint_color],
    'condition': [condition],
    'cylinders': [cylinders]
})

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Price: ${round(prediction, 2)}")
    