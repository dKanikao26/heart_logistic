import pickle
import pandas as pd
from fastapi import  FastAPI
from pydantic import BaseModel , Field
from typing_extensions import Annotated


app = FastAPI()

from joblib import load

model = load('model3.joblib')


class HealthInput(BaseModel):
    male: Annotated[int, Field(..., description="1 for male, 0 for female")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the individual in years")]
    education: Annotated[int, Field(..., ge=1, le=5, description="Education level (1 to 5)")]
    currentSmoker: Annotated[int, Field(..., description="1 if currently a smoker, else 0")]
    cigsPerDay: Annotated[float, Field(..., ge=0, description="Number of cigarettes per day")]
    BPMeds: Annotated[int, Field(..., description="1 if on blood pressure medication, else 0")]
    prevalentStroke: Annotated[int, Field(..., description="1 if history of stroke, else 0")]
    prevalentHyp: Annotated[int, Field(..., description="1 if has hypertension, else 0")]
    diabetes: Annotated[int, Field(..., description="1 if has diabetes, else 0")]
    totChol: Annotated[float, Field(..., gt=0, description="Total cholesterol level (mg/dL)")]
    sysBP: Annotated[float, Field(..., gt=0, description="Systolic blood pressure (mmHg)")]
    diaBP: Annotated[float, Field(..., gt=0, description="Diastolic blood pressure (mmHg)")]
    BMI: Annotated[float, Field(..., gt=0, lt=60, description="Body Mass Index")]
    heartRate: Annotated[float, Field(..., gt=0, lt=220, description="Heart rate (beats per minute)")]
    glucose: Annotated[float, Field(..., gt=0, description="Glucose level (mg/dL)")]
 

@app.post("/predict")
def results(data : HealthInput):
    input_dict = data.dict()
    df = pd.DataFrame([input_dict])

    res = model.predict(df)
    return res

