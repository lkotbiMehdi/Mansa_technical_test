from pydantic import BaseModel, validator
from typing import List
from datetime import date
from RegressionModel import RegressionModel


class Account(BaseModel):
    update_date: date
    balance: float


class Transaction(BaseModel):
    amount: float
    date: date


class RequestPredict(BaseModel):
    account: Account
    transactions: List[Transaction]

    @validator("transactions")
    def validate_transaction_history(cls, v, *, values):
        """
        validate that 
         - the transaction list passed has at least 6 months history
         - no transaction is posterior to the account's update date
        """
        if len(v) < 1:
            raise ValueError("Must have at least one transaction")

        update_t = values["account"].update_date

        oldest_t = v[0].date
        newest_t = v[0].date
        for t in v[1:]:
            if t.date < oldest_t:
                oldest_t = t.date
            if t.date > newest_t:
                newest_t = t.date

        assert (
            update_t - newest_t
        ).days >= 0, "Update Date Inconsistent With Transaction Dates"
        assert (update_t - oldest_t).days > 183, "Not Enough Transaction History"

        return v


class ResponsePredict(BaseModel):
    predicted_amount: float


def predict(
        transactions: List[Transaction], account: Account, model: RegressionModel
) -> float:
    return model.predict(transactions, account)
