from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.datasets import load_iris

app = Flask(__name__)

# Load the model from the file
with open('model_klasifikasi.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the iris dataset for target names and feature names
iris = load_iris()
feature_names = iris.feature_names

@app.route('/classify', methods=['POST'])
def classify():
    try:
        # Get data from the request
        data = request.json
        
        # Extract feature values in the correct order
        features = [data[feature] for feature in feature_names]
        features = np.array(features).reshape(1, -1)

        # Predict the class
        prediction = model.predict(features)
        predicted_class = iris.target_names[prediction][0]

        # Return the result as JSON
        return jsonify({'predicted_class': predicted_class})
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {str(e)}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
