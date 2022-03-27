from RegressionModel import RegressionModel
from pyDanticObjects import predict, RequestPredict
from fastapi import FastAPI

import yaml

config = yaml.safe_load(open('config.yml'))

app = FastAPI()
model = RegressionModel(config['model']['modelPath'])
    
@app.post("/predict")
async def root(predict_body: RequestPredict):
    transactions = predict_body.transactions
    account = predict_body.account
    v = predict(transactions, account, model)
    return {"predicted_amount": float(v)}
