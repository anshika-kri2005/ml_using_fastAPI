from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

# Load the saved model
model = joblib.load("iris_model.joblib")

# Create a FastAPI instance
app = FastAPI(title="Iris Classifier API")

# Define request body using Pydantic
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define the prediction endpoint
@app.post("/predict")
def predict_species(features: IrisFeatures):
    try:
        # Prepare input for the model
        data = [[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]]
        
        # Get prediction
        prediction = model.predict(data)
        
        # Map numerical output to species name
        species = ["setosa", "versicolor", "virginica"]
        return {"prediction": species[prediction[0]]}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
