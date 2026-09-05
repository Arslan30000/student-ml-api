from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="student-ml-api")

class PredictRequest(BaseModel):
    value: float

def get_version():
    try:
        with open("VERSION", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "1.1.0"

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": get_version(),
        "model version": "model-1"
    }

@app.post("/predict")
def predict(request: PredictRequest):
    return {"input": request.value, "prediction": request.value * 2}