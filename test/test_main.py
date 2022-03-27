import json
from datetime import date
import pickle
import requests


def test_predict():
    """
    Test the predict route with test data
    """

    # ----------ARTIFICIEL DATA-----------
    
    test_account = {"balance": 10000, "update_date": str(date(2020, 11, 3))}
    test_transactions = [
        {"date": str(date(2020, i, j)), "amount": -100}
        for i in range(1, 10)
        for j in [5,17,26]
    ]

    test_data = {
        "account": test_account,
        "transactions": test_transactions,
    }

    print("Calling API with test data:")
    print(test_data)

    response = requests.post(
        "http://127.0.0.1:8000/predict", data=json.dumps(test_data)
    )

    print("Response: ")
    print(response.json())

    assert response.status_code == 200

    # ----------REAL DATA-----------

    data = pickle.load(open('../bin/api_test_data.pkl', 'rb'))
    unprocessable = []
    response_codes = pickle.load(open('../bin/test_api_response_codes.pkl', 'rb'))
    for (account, transactions), response_code in zip(data, response_codes):
        test_data = {
            "account": account,
            "transactions": transactions,
        }
        print("Calling API with test data:")
        print(test_data)
        
        response = requests.post(
            "http://127.0.0.1:8000/predict", data=json.dumps(test_data)
        )
        
        print("Response: ")
        print(response.json())
        
        assert response.status_code == response_code
    
if __name__ == "__main__":
    test_predict()
