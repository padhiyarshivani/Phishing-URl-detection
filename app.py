from flask import Flask, request, render_template
import joblib
import numpy as np
from feature import FeatureExtraction  # Ensure this is defined and in your project

app = Flask(__name__)

# Load the trained model
model = joblib.load("pickle/model.pkl")  # Ensure correct path and file

def extract_features(url):
    # Extracts 30 features from URL using your custom module
    extractor = FeatureExtraction(url)
    return extractor.getFeaturesList()

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    url = None

    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        features = np.array(features).reshape(1, -1)

        result = model.predict(features)[0]
        prob_phishing = model.predict_proba(features)[0][0]
        prob_legitimate = model.predict_proba(features)[0][1]

        confidence = round((prob_phishing if result == -1 else prob_legitimate) * 100, 2)
        prediction = "Phishing" if result == -1 else "Legitimate"

    return render_template("index.html", prediction=prediction, confidence=confidence, url=url)

if __name__ == "__main__":
    app.run(debug=True)
