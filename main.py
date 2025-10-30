import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=ImportWarning)

import streamlit as st
import pickle
import numpy as np

# ----------------------------
# Load trained model
# ----------------------------
with open("balanced_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🍷 Wine Quality Prediction App")
st.write("Enter the wine’s chemical properties below to predict its quality category.")

# ----------------------------
# Input fields for all features
# ----------------------------
fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=20.0, value=7.0)
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=2.0, value=0.7)
citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=1.0, value=0.3)
residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=15.0, value=2.5)
chlorides = st.number_input("Chlorides", min_value=0.0, max_value=1.0, value=0.08)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0, max_value=100, value=30)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0, max_value=300, value=115)
density = st.number_input("Density", min_value=0.9, max_value=1.5, value=0.995)
pH = st.number_input("pH", min_value=2.0, max_value=5.0, value=3.2)
sulphates = st.number_input("Sulphates", min_value=0.0, max_value=2.0, value=0.6)
alcohol = st.number_input("Alcohol", min_value=0.0, max_value=20.0, value=10.0)

# ----------------------------
# Predict button
# ----------------------------
if st.button("Predict Quality"):
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                            chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                            density, pH, sulphates, alcohol]])
    
    prediction = model.predict(input_data)[0]

    # Map class names for better display
    if prediction == "low":
        st.error("🍷 This wine is predicted to be of **LOW quality**.")
    elif prediction == "medium":
        st.warning("🍇 This wine is predicted to be of **MEDIUM quality**.")
    else:
        st.success("🏆 This wine is predicted to be of **HIGH quality**!")
