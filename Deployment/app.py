from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained RandomForestClassifier model
loaded_model = joblib.load('random_forest_model.joblib')

# Define an API endpoint for predictions
@app.route('/predictliver', methods=['POST'])
def predictliver():
    # Extract feature values from the form data
    total_bilirubin = float(request.form.get('Total Bilirubin'))
    direct_bilirubin = float(request.form.get('Direct_Bilirubin'))
    alkaline_phosphotase = float(request.form.get('Alkaline_Phosphotase'))
    alamine_aminotransferase = float(request.form.get('Alamine_Aminotransferase'))
    total_protiens = float(request.form.get('Total_Protiens'))
    albumin = float(request.form.get('Albumin'))
    albumin_and_globulin_ratio = float(request.form.get('Albumin_and_Globulin_Ratio'))

    # Make prediction using the loaded model
    features = [total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase, total_protiens, albumin, albumin_and_globulin_ratio]
    prediction = loaded_model.predict([features])[0]

    # Render the result page with the prediction text
    return render_template('result.html', prediction_text=prediction)

# Render the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(host='192.168.174.33', port=5000, debug=True)
   # app.run(port=5000, debug=False)