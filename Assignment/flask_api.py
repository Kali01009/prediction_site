import os
import sys
import subprocess

from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the model
with open(os.path.join(sys.path[0], 'RSLModel.pkl'), 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    year_input = data['year']
    
    # Make predictions for the specified year
    X_future = pd.DataFrame({'year': [year_input]})
    future_value = model.predict(X_future)
    
    return jsonify({'prediction': future_value[0]})

def handler(event, context):
    from flask import jsonify
    from werkzeug.serving import run_simple

    if not os.path.exists("/tmp/pip"):
        os.makedirs("/tmp/pip")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", os.path.join(sys.path[0], "requirements.txt"), "-t", "/tmp/pip"])
    sys.path.append("/tmp/pip")
    
    return run_simple('0.0.0.0', 5000, app)

if __name__ == '__main__':
    app.run(debug=True)
