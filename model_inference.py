import pandas as pd
from flask import Flask, request

from joblib import load
import sklearn


model = load("./models/model1.joblib")
predictors_metadata = load("./models/model1_predictors_metadata.joblib")
var_list = list(predictors_metadata.keys())
print("Loaded model")

def validate_predictors(preds, metadata):
    new_data_metadata = preds.dtypes.to_dict()

    # Implement this
    all(test_dict1.get(key, None) == val for key, val
                                 in test_dict2.items())
    return True

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    # Get json from request and convert to a pd.DataFrame
    content = request.get_json()
    predictors_df = pd.json_normalize(content)
    print(predictors_df)

    valid = True #validate_predictors(predictors_df, predictors_metadata)

    # Use the model to predict if the data is valid
    if valid:
        house_value = model.predict(predictors_df[var_list])[0]
        retval = {"Predicted_House_Value":house_value}
    else:
        retval = {"Predicted_House_Value":"INVALID_DATA"}

    return(retval)

@app.route('/ping', methods=['GET'])
def ping():
    return("healthy")

if __name__ == '__main__':
    app.run()
