import pandas as pd
from flask import Flask, request

from joblib import load
import sklearn

model = load("./models/model1.joblib")
var_list = model.feature_names_in_


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    # Get json from request and convert to a pd.DataFrame
    predictors = request.get_json()
    predictors_df = pd.DataFrame(predictors, index = [0])

    # Use the model to predict, using only the vars in the model
    #print(predictors_df)
    house_value = model.predict(predictors_df[var_list])[0]

    return({"Predicted_House_Value":house_value})


if __name__ == '__main__':
    app.run()
