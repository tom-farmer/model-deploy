import requests
import json

def main():
    """
    Assumes that the flask app is running locally already
    """
    # app running locally on port 5000
    url = 'http://localhost:5000/predict'

    preds = {"OverallQual":10,
             "OverallCond":5,
             "TotalBsmtSF":1000,
             "FullBath":4}

    r = requests.post(url, json = preds)

    print(r.json())


if __name__ == "__main__":
    main()
