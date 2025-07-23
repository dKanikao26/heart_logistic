import streamlit as st
import requests

st.set_page_config(page_title="Heart Disease Risk Predictor", layout="centered")

st.title("Heart Disease 10-Year CHD Risk Predictor")
st.markdown(
    "Enter your health information below to estimate your risk of coronary heart disease in the next 10 years."
)

with st.form("risk_form"):
    male = st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    age = st.number_input("Age", 1, 119, value=50)
    education = st.select_slider("Education Level (1–5)", options=[1, 2, 3, 4, 5], value=3)
    currentSmoker = st.checkbox("Currently Smoking?")
    cigsPerDay = st.number_input("Cigarettes per Day", 0.0, 100.0, value=0.0)
    BPMeds = st.checkbox("On Blood Pressure Medication?")
    prevalentStroke = st.checkbox("History of Stroke?")
    prevalentHyp = st.checkbox("Has Hypertension?")
    diabetes = st.checkbox("Has Diabetes?")
    totChol = st.number_input("Total Cholesterol (mg/dL)", 50.0, 700.0, value=200.0)
    sysBP = st.number_input("Systolic BP (mmHg)", 50.0, 300.0, value=120.0)
    diaBP = st.number_input("Diastolic BP (mmHg)", 30.0, 200.0, value=80.0)
    BMI = st.number_input("Body Mass Index", 10.0, 60.0, value=26.0)
    heartRate = st.number_input("Heart Rate (bpm)", 20.0, 220.0, value=72.0)
    glucose = st.number_input("Glucose Level (mg/dL)", 40.0, 300.0, value=85.0)
    submit = st.form_submit_button("Predict CHD Risk")

if submit:
    # Prepare input dictionary matching FastAPI HealthInput
    payload = {
        "male": male,
        "age": age,
        "education": education,
        "currentSmoker": int(currentSmoker),
        "cigsPerDay": cigsPerDay,
        "BPMeds": int(BPMeds),
        "prevalentStroke": int(prevalentStroke),
        "prevalentHyp": int(prevalentHyp),
        "diabetes": int(diabetes),
        "totChol": totChol,
        "sysBP": sysBP,
        "diaBP": diaBP,
        "BMI": BMI,
        "heartRate": heartRate,
        "glucose": glucose
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            risk = "🚨 High Risk" if result["prediction"] == 1 else "✅ Low Risk"
            st.success(f"**Prediction:** {risk}")
            st.info(f"**Predicted Probability:** {result['probability']:.2f}")
        else:
            st.error("Server error: Received status code " + str(response.status_code))
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI backend at http://localhost:8000")

