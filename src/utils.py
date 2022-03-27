from datetime import timedelta
from datetime import datetime as dt

def getBalances(last_balance, outGoings, inGoings):
    """
    A utility function that calculates balance per day 

    IN : last_balance (float), outGoings (dict), inGoings (dict)
    OUT : record (dict)
    """
    balance = {}
    current_balance = last_balance
    # reverse engineering balance
    for (date, ingoing), (_, outgoing) in zip(inGoings.items(), outGoings.items()):
        current_balance = current_balance - abs(ingoing) + abs(outgoing)
        balance[date] = current_balance
    return balance

def calculateLastAmounts(records, n_months=5, is_balance=False):
    """
    A utility function that calculates values per month for the last n_months of the record 

    IN : records (dict)
    OUT : values (list of n_months element)
    """
    v = list(records.values())
    n = len(v)
    # hypothesis : 1 month == 30 days
    if is_balance:
        retVal = [v[n-i*30-1] for i in range(n_months)]
    else:
        retVal = [sum(v[n-i*30: n-(i-1)*30]) for i in range(1, n_months+1)]
    return retVal

def correctDateRecord(record, start_date, end_date):
    """
    A utility function that transforms a list of the form {"date1": value, "date2": value....} by imputing
    missing dates with a value of 0. Missing dates are all of those from start_date to end_date that are not 
    in record.keys()

    IN : record (dict), start_date (datetime), end_date (datetime)
    OUT : record (dict)
    """
    list_dates = [start_date + timedelta(days=x) for x in range((end_date-start_date).days)]
    corrected_record = [[day, record[day]] if day in list(record.keys()) else [day, 0] for day in list_dates]
    return dict(corrected_record)

def getDateInterval(outGoings, inGoings, update_date):
    """
    A utility function that calculates min and max date keys in the two records outGoings and inGoings
    for which the keys are sorted dates

    IN : inGoings (record), outGoings (record), update_date (str)
    OUT : (min_date, max_date) (datetime, datetime)
    """
    # calculating max/min dates
    if len(inGoings)==0:
        min_date = list(outGoings.keys())[0]
        max_date = list(outGoings.keys())[-1]
    elif len(outGoings)==0:
        min_date = list(inGoings.keys())[0]
        max_date = list(inGoings.keys())[-1]
    else:
        min_date = min(list(outGoings.keys())[0],
                       list(inGoings.keys())[0])
        max_date = min(list(outGoings.keys())[-1],
                       list(inGoings.keys())[-1])
    max_date = max(max_date, update_date)
    return min_date, max_date
