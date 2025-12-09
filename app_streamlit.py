import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction Web App")

st.write("Enter the car details below to predict the selling price.")

year = st.number_input("Year", min_value=1990, max_value=2025, value=2015)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, value=5.0)
kms = st.number_input("Driven Kilometers", min_value=0, value=50000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
selling_type = st.selectbox("Selling Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.number_input("Owner Count", min_value=0, max_value=3, value=0)

# Convert text inputs to numerical values (same as in training)
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
selling_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 0, "Automatic": 1}

fuel = fuel_map[fuel_type]
seller = selling_map[selling_type]
trans = trans_map[transmission]

input_data = np.array([[year, present_price, kms, fuel, seller, trans, owner]])

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Selling Price: ₹ {prediction:.2f} lakhs")
