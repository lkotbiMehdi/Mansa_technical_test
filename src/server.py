from RegressionModel import RegressionModel
from pyDanticObjects import predict, RequestPredict
from fastapi import FastAPI

    
app = FastAPI()
model = RegressionModel("../data/model_reg.pkl")
    
@app.post("/predict")
async def root(predict_body: RequestPredict):
    transactions = predict_body.transactions
    account = predict_body.account
    v = predict(transactions, account, model)
    return {"predicted_amount": float(v)}
