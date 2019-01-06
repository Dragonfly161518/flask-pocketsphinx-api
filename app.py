# Dependencies
from flask import Flask, request, jsonify
import traceback
import pandas as pd
import numpy as np

import deepcut 

# Your API definition
app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    return jsonify({'prediction': 'test'})

@app.route('/predict', methods=['POST'])
def predict():
    if True:
        try:
            json_ = request.json
            return jsonify({'prediction': deepcut.tokenize(json_['text'])})
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    app.run()