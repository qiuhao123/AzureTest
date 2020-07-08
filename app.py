import numpy as np
import pickle
from flask import Flask, request,jsonify, render_template
import json
import requests
from ast import literal_eval

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [int_features]
    #return type(''.join(final_features))
    scoring_uri = 'http://43aa851b-4045-482b-9016-9f97cc6b3e70.westus2.azurecontainer.io/score'

    #prediction = model.predict(final_features)
    data = {"data":final_features}
    #return ''.join(data)
    input_data = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    resp = requests.post(scoring_uri, input_data, headers=headers)
    prediction = "the value should be" + resp.text

    #
    return render_template('home.html', prediction_text= prediction)
if __name__ == "__main__":
    app.run(debug=True)
