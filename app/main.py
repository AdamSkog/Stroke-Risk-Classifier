from fastapi import FastAPI
from pydantic import BaseModel, validator
import joblib
import pandas as pd
from app.utils.multicolle import MultiColumnLabelEncoder


app = FastAPI()


pipe = joblib.load('app/pipelines/xgb_pipeline.pkl')


class PredictionInput(BaseModel):
    Age: float
    Hypertension: int
    Heart_disease: int
    Avg_glucose_level: float
    Bmi: float
    Stroke: int
    Sex: str
    Marriage_status: str
    Employment: str
    Residency: str
    Smoker: str

    @validator('Age', 'Hypertension', 'Heart_disease',
               'Avg_glucose_level', 'Bmi', 'Stroke')
    def validate_non_negative(cls, value):
        if value < 0:
            raise ValueError("Input values must be non-negative")
        return value


@app.get("/")
def home():
    return {'health_check': 'OK'}


@app.post('/predict')
def predict(data: PredictionInput):
    input_data = pd.DataFrame([{
        'Age': data.Age,
        'Hypertension': data.Hypertension,
        'Heart_disease': data.Heart_disease,
        'Avg_glucose_level': data.Avg_glucose_level,
        'Bmi': data.Bmi,
        'Stroke': data.Stroke,
        'Sex': data.Sex,
        'Marriage_status': data.Marriage_status,
        'Employment': data.Employment,
        'Residency': data.Residency,
        'Smoker': data.Smoker
    }])

    prediction_result = pipe.predict(input_data)
    return {'prediction': prediction_result.tolist()}
