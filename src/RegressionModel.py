import pandas as pd
import numpy as np

import pickle
from utils import *

class RegressionModel(object):
    """
    Regression model class for predicting next month outgoings of a given account
    """
    def __init__(self, model_path):
        # load regression model
        self.__regressor = pickle.load(open(model_path, 'rb'))

    def predict(self, transactions, account):
        """
        Predicts the aggregated next month outgoing for the account based on it's transactions

        IN : transactions (dict), account (dict)
        OUT : pred (float)
        """
        # calculate features
        event = self.featureEngineering(transactions, account)
        # predict and return value
        pred = self.__regressor.predict(np.array(event).reshape(1, -1))
        return pred[0]

    def featureEngineering(self, transactions, account):
        """
        Generates model's input features from a transactions & account records
        
        IN : transaction (dict), account (dict)
        OUT : event (list of calculated features)
        """
        # gathering data points together
        data = pd.DataFrame(map(dict, transactions))
        data['balance'] = account.balance
        data['update_date'] = account.update_date
        
        # aggregatin/calculating outgoings/ingoings
        outGoings = dict(data[data.amount < 0].groupby('date', sort=True)\
                                         .agg({'amount': 'sum'}).to_records())
        inGoings = dict(data[data.amount > 0].groupby('date', sort=True)\
                                         .agg({'amount': 'sum'}).to_records())

        min_date, max_date = getDateInterval(outGoings, inGoings, account.update_date)
        
        # making the three records of the same length (min_date -> max_date)
        outGoings = correctDateRecord(outGoings, min_date, max_date)
        inGoings = correctDateRecord(inGoings, min_date, max_date)
        balances = getBalances(data['balance'].values[0], outGoings, inGoings)
        
        # calculating last n amounts for outgoings, ingoings and balances
        x_outgoings = calculateLastAmounts(outGoings)
        x_ingoings = calculateLastAmounts(inGoings)
        x_balances = calculateLastAmounts(balances, is_balance=True)
            
        return x_outgoings + x_ingoings + x_balances

    
