from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc

mlflow.set_tracking_uri('data')

class InputText(BaseModel):
    input_texts: str

app = FastAPI()

@app.get("/health")
def get_health():
    return {"status": "OK"}

@app.post("/get-prediction/")
def get_prediction(input_data: InputText):
    # TODO - task 2 
    # -----------------------------------
    # Goal: our goal is to complete the implementation of this function, 
    #       which takes input data and returns a prediction result from a pre-trained model.
    pass