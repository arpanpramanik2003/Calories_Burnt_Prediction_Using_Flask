from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Loading trained machine learning model
model = pickle.load(open('P:/Documents(p)/Web_Development/HTML_CODE/Calories_Burnt/calories_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = request.form.get('gender')
    age = float(request.form.get('age'))
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    duration = float(request.form.get('duration'))
    heartrate = float(request.form.get('heartrate'))
    temp = float(request.form.get('temp'))

    gender_map = {'male': 0, 'female': 1}
    gender = gender_map.get(gender.lower(), -1)

    # Checking  for invalid gender input
    if gender == -1:
        return render_template('index.html', prediction_text="Invalid gender selected.")

    features = [[gender, age, height, weight, duration, heartrate, temp]]

    prediction = model.predict(features)[0]

    return render_template('index.html', prediction_text=f"Predicted Calories Burnt: {prediction:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
