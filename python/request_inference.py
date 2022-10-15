import requests
import pandas as pd
import numpy as np
import random
from joblib import load

test = pd.read_csv('./data/test.csv')

# Assume that whoever is requesting knows the data types and variable names
# to send to the API
load("./models/model1_predictors_metadata.joblib")
url = 'http://localhost:5000/predict'

def main():
    custom_data_request()
    #random_test_data_request()
    #pass

def custom_data_request():
    """
    Sends an http post request that gets the predicted value of a house
    Assumes that the flask app is running locally already on port 5000
    """

    preds = {"OverallQual":int(5.97623),
             "OverallCond":int(5),
             "TotalBsmtSF":1000,
             "FullBath":3,
             "YearBuilt":1993}

    r = requests.post(url, json = preds)
    print(r.json())

def random_test_data_request():

    # Get a random row
    randrow = random.randint(0,test.shape[0]-1)

    # Pull the row and convert it to a dictionary
    preds = test.iloc[randrow].to_dict()
    print([type(preds[idx]) for idx in preds])
    r = requests.post(url, json = preds)

    print(r.json())

    pass

if __name__ == "__main__":
    main()
