import streamlit as st
import numpy as np
import pandas as pd

# Page config
st.set_page_config(page_title="California House Price Prediction", page_icon="🏠", layout="centered")

# Header
st.markdown(
    """
    <h1 style='text-align:center; color:#2E86C1;'>California House Price Prediction</h1>
    <p style='text-align:center; color:gray;'>TensorFlow removed — this version uses a dummy model for quick testing.</p>
    """ ,
    unsafe_allow_html=True
)

# Sidebar inputs
st.sidebar.header("Input Features")

Longitude = st.sidebar.slider("Longitude", -125.0, -113.0, -120.0)
Latitude = st.sidebar.slider("Latitude", 32.0, 42.0, 37.0)
Housing_median_age = st.sidebar.slider("Median Age", 1, 50, 20)
Total_rooms = st.sidebar.number_input("Total Rooms", 1, 10000, 1000)
Total_bedrooms = st.sidebar.number_input("Total Bedrooms", 1, 2000, 300)
Population = st.sidebar.number_input("Population", 1, 10000, 500)
Households = st.sidebar.number_input("Households", 1, 5000, 300)
Median_income = st.sidebar.slider("Median Income (10k USD)", 0.0, 15.0, 3.5)

# Prepare input
input_data = np.array([[Longitude, Latitude, Housing_median_age,
                        Total_rooms, Total_bedrooms, Population,
                        Households, Median_income]])

# Dummy prediction formula (for demo)
predicted_price = (Median_income * 100000) + (Housing_median_age * 500) + np.random.randint(10000, 90000)

# Display prediction
if st.button("Predict Price"):
    st.success(f"🏡 Estimated House Price: **${predicted_price:,.2f}**")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align:center; color:gray;'>
    Built with ❤️ using Streamlit
    </p>
    """ ,
    unsafe_allow_html=True
)
