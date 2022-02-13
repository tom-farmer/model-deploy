import pandas as pd
from flask import Flask, request

from joblib import load
import sklearn

model = load("./models/model.joblib")
var_list = load("./models/var_list.joblib")


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    predictors = request.get_json()
    predictors_df = pd.DataFrame(predictors, index = [0])

    print(predictors_df)
    house_value = model.predict(predictors_df[var_list])

    return({"Predicted_House_Value":house_value[0]})


if __name__ == '__main__':
    app.run()
