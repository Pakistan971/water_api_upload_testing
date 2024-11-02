from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

app = FastAPI(
    title= "Water Potability Prediction",
    description = "Predicting Water Potability"
)

with open(r"C:\Users\Shahbaz\Desktop\MLops\Video 2 Project\model.pkl","rb") as f:
    model = pickle.load(f)

@app.get("/")
#for homepage
def index():
    return "Welcome to Water Potability Prediction FastAPI"

@app.post("/predict")
# water:Water means water is obj of Water and must contain
#properties defined in Water class in the data_model.py file
def model_predict(water: Water):
    sample = pd.DataFrame({
        'ph': [water.ph],
        'Hardness':[water.Hardness],
        'Solids':[water.Solids],
        'Chloramines':[water.Chloramines],
        'Sulfate':[water.Sulfate],
        'Conductivity':[water.Conductivity],
        'Organic_carbon':[water.Organic_carbon],
        'Trihalomethanes':[water.Trihalomethanes],
        'Turbidity':[water.Turbidity]
    })

    predicted_sample = model.predict(sample)

    # if predicted_sample == 1:
    #     return "Water is Consumable"

    # else:
    #     return "Water is Not Consumable"

    return "Water is Consumable" if predicted_sample == 1 else "Water is Not Consumable"
