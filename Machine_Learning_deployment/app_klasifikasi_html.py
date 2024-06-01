from flask import Flask, request, render_template
import joblib

# Load the trained model
clf = joblib.load('model_klasifikasi.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_klasifikasi_styled.html')

# class_mapping = {
#     0: 'setosa',
#     1: 'versicolor',
#     2: 'virginica'
# }

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    try:
        features = [float(data['sepal_length']), float(data['sepal_width']), float(data['petal_length']), float(data['petal_width'])]
        prediction = clf.predict([features])
        result = {
            'prediction': int(prediction[0])
        }
        return render_template('index_klasifikasi_styled.html', result=result)
    except KeyError as e:
        return render_template('index_klasifikasi_styled.html', error=f"Missing feature: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
