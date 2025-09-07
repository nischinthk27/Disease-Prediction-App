import requests

url = "http://127.0.0.1:5000/predict"

# Input data (must match FEATURE_ORDER in app.py)
data = {
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 79,
    "BMI": 25.3,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 33
}

# Send request as JSON
response = requests.post(url, json=data)

# Print response from Flask API
print(response.json())
