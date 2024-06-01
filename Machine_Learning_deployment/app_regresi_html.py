from flask import Flask, request, render_template
import joblib

# Load the trained model
regressor = joblib.load('model_regresi.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_regresi_styled.html', prediction=None, error=None)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    try:
        features = [float(data[feat]) for feat in data]
        prediction = regressor.predict([features])[0]
        return render_template('index_regresi_styled.html', prediction=prediction, error=None)
    except Exception as e:
        return render_template('index_regresi_styled.html', prediction=None, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
