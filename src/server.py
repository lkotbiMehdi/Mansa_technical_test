from RegressionModel import RegressionModel
from pyDanticObjects import predict, RequestPredict
from fastapi import FastAPI
import uvicorn

from environs import Env

# Read env file
env = Env()
env.read_env(".env")

app = FastAPI()
model = RegressionModel(env.str("MODEL_PATH"))
    
@app.post("/predict")
async def root(predict_body: RequestPredict):
    transactions = predict_body.transactions
    account = predict_body.account
    v = predict(transactions, account, model)
    return {"predicted_amount": float(v)}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
