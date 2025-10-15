from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle

# --- Load Models ---
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Initialize FastAPI app ---
app = FastAPI(title="Ride Surge Prediction API")

# --- Input schema ---
class RideData(BaseModel):
    distance: float
    temperature: float
    hour: int
    rainfall: float

@app.get("/")
def home():
    return {"message": "Ride Surge Prediction API is running!"}

@app.post("/predict")
def predict(data: RideData):
    # Convert to DataFrame
    df = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
    
    # Scale input
    scaled = scaler.transform(df)
    
    # Predict using model
    pred = model.predict(scaled)[0]
    
    return {"surge_prediction": float(pred)}
