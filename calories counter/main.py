import requests
from datetime import datetime

API_KEY = "6afa158fd32cab2ac27822ff949c97bc"
APP_ID = "cb5fc7d8"

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "174"
AGE = "28"
MY_EMAIL = "r4z0r3583@gmail.com"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f12db651d04becf72b24914c2120322f/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
     sheet_inputs = {
         "workout": {
             "date": today_date,
             "time": now_time,
             "exercise": exercise["name"].title(),
             "duration": exercise["duration_min"],
             "calories": exercise["nf_calories"]
         }
     }


sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

