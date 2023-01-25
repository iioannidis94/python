import requests

QUESTION_AMOUNT = 50

parameters = {
    "amount": QUESTION_AMOUNT,
    "type": "boolean"
    # "category": 18
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
