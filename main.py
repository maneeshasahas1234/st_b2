


import joblib
import streamlit as st


st.title('Home Price Prediction')

model = joblib.load('model.pkl')

area = st.number_input("Area (sq ft)", value=1000)
bedrooms = st.number_input("Number of Bedrooms", value=2, step=1)
age = st.number_input("Age of House (years)", value=10)

if st.button('Predict'):
    prediction = model.predict([[area, bedrooms, age]])
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")













