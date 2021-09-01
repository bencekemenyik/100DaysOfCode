import requests
from datetime import datetime
# import os

# APP_ID = os.environ["APP_ID"]
# API_KEY = os.environ["API_KEY"]
# GOOGLE_SHEET_ENDPOINT = os.environ["GOOGLE_SHEET_ENDPOINT"]
# BEARER_TOKEN = os.environ["BEARER_TOKEN"]

APP_ID = "your-app-id"
API_KEY = "your-api-key"
BEARER_TOKEN = "your-bearer-token"
GOOGLE_SHEET_ENDPOINT = "sheety-google-sheet-endpoint"

EXERCISE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

data = input("What kind of exercises you did today?")

parameters = {
    "query": data,
    "gender": "male",
    "weight_kg": 85.5,
    "height_cm": 180,
    "age": 22
}

response = requests.post(url=EXERCISE_END_POINT, json=parameters, headers=headers)
result = response.json()
# print(result["exercises"][0])

exercises = result["exercises"]

today = datetime.now()
today_date = today.strftime('%d/%m/%Y')
today_now = today.strftime('%X')

auth_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in exercises:
    sheet_data = {
        "munkalap1": {
            "date": today_date,
            "time": today_now,
            "exercise": f"{exercise['user_input'].title()}",
            "duration": f"{exercise['duration_min']}",
            "calories": f"{exercise['nf_calories']}",
        }
    }

    requests.post(url=GOOGLE_SHEET_ENDPOINT, json=sheet_data, headers=auth_headers)
    print(exercise)



