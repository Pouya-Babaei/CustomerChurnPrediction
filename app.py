import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json


with open("models/config.json", "r") as f:
    config = json.load(f)

FINAL_THRESHOLD = config["threshold"]

model = joblib.load("models/logistic_regression_pipeline.joblib")

app = FastAPI(title="Customer Churn Prediction API", version="1.0.0")


class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/model-info")
def model_info():
    return {
        "model_name": "Logistic Regression",
        "version": "1.0.0",
        "task": "Customer Churn Classification",
        "threshold": FINAL_THRESHOLD
    }


@app.post("/predict")
def pred(data: CustomerData):

    sample = [[
        data.gender,
        data.SeniorCitizen,
        data.Partner,
        data.Dependents,
        data.tenure,
        data.PhoneService,
        data.MultipleLines,
        data.InternetService,
        data.OnlineSecurity,
        data.OnlineBackup,
        data.DeviceProtection,
        data.TechSupport,
        data.StreamingTV,
        data.StreamingMovies,
        data.Contract,
        data.PaperlessBilling,
        data.PaymentMethod,
        data.MonthlyCharges,
        data.TotalCharges
    ]]

    sample = pd.DataFrame(
        sample,
        columns=[
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges"
        ]
    )

    probability = model.predict_proba(sample)[0][1]

    prediction = probability >= FINAL_THRESHOLD

    return {
    "probability": float(probability),
    "threshold": FINAL_THRESHOLD,
    "prediction": bool(prediction)
    }

