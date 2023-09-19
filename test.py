import requests
import json

# Define the base URL for your FastAPI app
base_url = "http://localhost:8000"  # Replace with the correct URL

# Define your mock data as a dictionary
mock_data = {
    "Age": 45.0,
    "Hypertension": 0,
    "Heart_disease": 1,
    "Avg_glucose_level": 85.0,
    "Bmi": 28.5,
    "Stroke": 0,
    "Sex": "Male",
    "Marriage_status": "Married",
    "Employment": "Employed",
    "Residency": "Urban",
    "Smoker": "No"
}

# Convert the mock data to a JSON string
json_data = json.dumps(mock_data)

# Send a POST request to your FastAPI endpoint with the JSON data
headers = {"Content-Type": "application/json"}
response = requests.post(f"{base_url}/predict", data=json_data, headers=headers)

# Check the response status code and content
if response.status_code == 200:
    print("Prediction result:")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
