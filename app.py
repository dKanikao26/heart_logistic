import streamlit as st
import requests

st.title('Health Risk Predictor')

with st.form('health_form'):
    male = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    age = st.number_input('Age', min_value=1, max_value=119, value=30)
    education = st.slider('Education level', min_value=1, max_value=5, value=3)
    currentSmoker = st.checkbox('Currently Smoking')
    cigsPerDay = st.number_input('Cigarettes per day', min_value=0.0, value=0.0)
    BPMeds = st.checkbox('On Blood Pressure Medication')
    prevalentStroke = st.checkbox('History of Stroke')
    prevalentHyp = st.checkbox('Has Hypertension')
    diabetes = st.checkbox('Has Diabetes')
    totChol = st.number_input('Total Cholesterol (mg/dL)', min_value=0.1, value=150.0)
    sysBP = st.number_input('Systolic Blood Pressure (mmHg)', min_value=0.1, value=120.0)
    diaBP = st.number_input('Diastolic Blood Pressure (mmHg)', min_value=0.1, value=80.0)
    BMI = st.number_input('Body Mass Index', min_value=0.1, max_value=59.9, value=22.0)
    heartRate = st.number_input('Heart Rate (beats per minute)', min_value=1.0, max_value=219.9, value=70.0)
    glucose = st.number_input('Glucose Level (mg/dL)', min_value=0.1, value=100.0)

    submitted = st.form_submit_button('Predict')

if submitted:
    payload = {
        'male': male,
        'age': age,
        'education': education,
        'currentSmoker': int(currentSmoker),
        'cigsPerDay': cigsPerDay,
        'BPMeds': int(BPMeds),
        'prevalentStroke': int(prevalentStroke),
        'prevalentHyp': int(prevalentHyp),
        'diabetes': int(diabetes),
        'totChol': totChol,
        'sysBP': sysBP,
        'diaBP': diaBP,
        'BMI': BMI,
        'heartRate': heartRate,
        'glucose': glucose
    }

    response = requests.post('http://localhost:8000/predict', json=payload)
    if response.status_code == 200:
        st.success(f'Prediction: {response.json()}')
    else:
        st.error('Prediction failed')
