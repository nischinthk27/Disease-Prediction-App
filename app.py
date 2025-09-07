from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

# Define feature order (same as in diabetes.csv)
FEATURE_ORDER = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.is_json:
            # Input from API (JSON)
            data = request.get_json()
            features = [float(data[feature]) for feature in FEATURE_ORDER]
        else:
            # Input from form (HTML)
            features = [float(request.form[feature]) for feature in FEATURE_ORDER]

        # Convert to numpy array
        final_features = np.array(features).reshape(1, -1)

        # Get prediction probability
        prob = model.predict_proba(final_features)[0][1]

        if prob >= 0.5:
            prediction_text = "✅ Disease Present"
        else:
            prediction_text = "🟢 No Disease"

        probability_text = f"Prediction Confidence: {prob*100:.2f}%"

        # Return JSON if API call
        if request.is_json:
            return jsonify({"prediction": prediction_text, "confidence": probability_text})
        else:
            return render_template("index.html", prediction_text=prediction_text, probability_text=probability_text)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
