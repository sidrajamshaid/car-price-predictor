import streamlit as st
import pandas as pd
import joblib

# ✅ Set up page configuration (must be FIRST Streamlit command)
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

# ✅ Optional: Apply custom CSS if file exists
try:
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ✅ Load trained model pipeline
model = joblib.load("car_price_model.pkl")

# ✅ App title and description
st.title("🚗 Car Price Predictor")
st.markdown("Fill in the car details to get an estimated market price 💰.")

# ✅ Sidebar input form
st.sidebar.header("🔧 Car Specifications")

year = st.sidebar.number_input("Year", min_value=1990, max_value=2025, value=2015)
odometer = st.sidebar.number_input("Odometer (miles)", min_value=0, max_value=300000, value=60000)

manufacturer = st.sidebar.selectbox("Manufacturer", ['ford', 'chevrolet', 'toyota', 'honda', 'nissan', 'jeep', 'other'])
fuel = st.sidebar.selectbox("Fuel Type", ['gas', 'diesel', 'electric', 'hybrid', 'other'])
transmission = st.sidebar.selectbox("Transmission", ['automatic', 'manual', 'other'])
drive = st.sidebar.selectbox("Drive Type", ['fwd', 'rwd', '4wd'])
car_type = st.sidebar.selectbox("Car Type", ['sedan', 'SUV', 'truck', 'hatchback', 'wagon', 'convertible', 'coupe', 'van', 'other'])
paint_color = st.sidebar.selectbox("Paint Color", ['black', 'white', 'silver', 'blue', 'red', 'grey', 'green', 'custom'])
condition = st.sidebar.selectbox("Condition", ['excellent', 'good', 'fair', 'like new', 'new', 'salvage'])
cylinders = st.sidebar.selectbox("Cylinders", ['4 cylinders', '6 cylinders', '8 cylinders', '3 cylinders', '5 cylinders'])

# ✅ Predict button
if st.button("🔍 Predict Car Price"):
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

    prediction = model.predict(input_data)[0]
    st.success(f"💸 Estimated Price: **${prediction:,.2f}**")