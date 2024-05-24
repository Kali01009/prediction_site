from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('RSLModel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    year_input = data['year']
    
    # Make predictions for the specified year
    X_future = pd.DataFrame({'year': [year_input]})
    future_value = model.predict(X_future)
    
    return jsonify({'prediction': future_value[0]})

if __name__ == '__main__':
    app.run(debug=True)
