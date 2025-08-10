import streamlit as st
import pandas as pd
import pickle
import base64
from sklearn.preprocessing import StandardScaler


def add_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("insurance.png")

st.markdown(
    """
    <div style='
        position: absolute;
        top: 50%;
        left: 5%;
        transform: translateY(-50%);
    '>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white;'>Medical Insurance Predictor</h1>", unsafe_allow_html=True)


with open("medical_cost_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)


with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


age_input = st.number_input("Enter Your Age", min_value=0, max_value=120, value=25)
sex_input = st.selectbox("Enter Your Gender", ("Male", "Female"))
bmi_input = st.number_input("Enter Your BMI", min_value=10.0, max_value=40.0, value=22.0, step=0.1)
children_input = st.number_input("Enter Number of Children", min_value=0, max_value=10, value=0)
smoker_input = st.radio("Are You A Smoker?", ("Yes", "No"))
region_input = st.selectbox("Enter Your Region", ("northeast", "northwest", "southeast", "southwest"))

if st.button("Predict"):
  
    sex = 0 if sex_input.lower() == "female" else 1
    smoker = 1 if smoker_input.lower() == "yes" else 0

    region_northeast = 1 if region_input == "northeast" else 0
    region_northwest = 1 if region_input == "northwest" else 0
    region_southeast = 1 if region_input == "southeast" else 0
    region_southwest = 1 if region_input == "southwest" else 0


    input_features = [[
        age_input,
        sex,
        bmi_input,
        children_input,
        smoker,
        region_northeast,
        region_northwest,
        region_southeast,
        region_southwest
    ]]


    input_features_scaled = scaler.transform(input_features)

    
    prediction = model.predict(input_features_scaled)

    st.markdown(
        f"""
        <div style='
            background-color: white;
            color:#2C3E50;
            padding: 14px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-top: 25px;
        '>
            Predicted Insurance Cost Is: {prediction[0]:.2f}$
        </div>
        """,
        unsafe_allow_html=True
    )
