"""
Note this file contains _NO_ flask functionality.
Instead it makes a file that takes the input dictionary Flask gives us,
and returns the desired result.

This allows us to test if our modeling is working, without having to worry
about whether Flask is working. A short check is run at the bottom of the file.
"""

import pickle
import numpy as np
import pandas as pd

# lr_model is our simple logistic regression model
# lr_model.feature_names are the four different iris measurements
with open("static/models/lr_tuned.pkl", "rb") as f:
    lr_model = pickle.load(f)
with open("static/models/scaler_sel.pkl","rb") as g:
    scaler = pickle.load(g)

feature_names = lr_model.feature_names
feature_display_names = lr_model.feature_display_names
# all of the attributes of the model are also saved in the pickle file
# like feature_names and target_names, which are all stored as key value pairs

def fund_extract(inputs):
    """
    Input:
    feature_dict: a dictionary of the form {"feature_name": "value"}

    Output:
    Returns list with the values corresponding to the first 4 feature columns
    """
    out = [float(inputs.get(name, 0)) for name in lr_model.feature_names[0:4]]
    out[1] *= 30
    out[2] *= 30
    return out
def convert(string,start,end):
    """
    Input: string for selected field, start/end index in feature column set

    Output: list of values corresponding to X_test[4:15]
    """
    vars = np.zeros(end-start)
    if string == "Other":
        return vars
    elif string in feature_names[start:end]:
        vars[list(feature_names[start:end]).index(string)] = 1
        return list(vars)

def make_prediction(x_input):
    """
    Input:
    feature_dict: a dictionary of the form {"feature_name": "value"}

    Function makes sure the features are fed to the model in the same order the
    model expects them.

    Output:
    Returns (x_inputs, probs) where
      x_inputs: a list of feature values in the order they appear in the model
      probs: a list of dictionaries with keys 'name', 'prob'
    """
    x_input_scaled = scaler.transform(np.array(x_input).reshape(1, -1))

# get is helpful - if somebody doesn't fill out one of the form entries then plug in zero
# a better guess than zero might be the average of that feature's distribution
# "if the key that is not found ==this, then plug in this"
    pred_probs = lr_model.predict_proba(x_input_scaled).flat

    probs = [{'name': lr_model.target_names[index], 'prob': pred_probs[index]}
    # list of dictionaries
    # dictionary comprehension
    # three dictionaries with two keys and two values each
    # can't sort within dictionaries, but can sort three separate dictionaries
             for index in np.argsort(pred_probs)[::-1]]
             # array sorted most likely to least likely class
             # 'name' gives the names of the classes
             # 'prob' gives its associated probability

    return probs


# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal.
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
if __name__ == '__main__':
    from pprint import pprint
    print("Checking to see what setting all params to 0 predicts")
    features = {f: '0' for f in feature_names}
    print('Features are')
    pprint(features)

    x_input, probs = make_prediction(features)
    print(f'Input values: {x_input}')
    print('Output probabilities')
    pprint(probs)
