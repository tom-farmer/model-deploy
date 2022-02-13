import requests
import json

def main():
    """
    Sends an http post request that gets the predicted value of a house
    Assumes that the flask app is running locally already on port 5000
    """
    url = 'http://localhost:5000/predict'

    preds = {"OverallQual":5,
             "OverallCond":5,
             "TotalBsmtSF":1000,
             "FullBath":3,
             "garbage_var":100}


    r = requests.post(url, json = preds)
    print(r.json())


if __name__ == "__main__":
    main()
