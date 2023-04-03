import requests
from datetime import datetime

TOKEN = "gc0ma8wo0aud123vXCvt6fg"
USERNAME = "razor1994"
GRAPH = "graph-2"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Read Pages",
    "unit": "Times",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create now date
now = datetime.now()
date_string = now.strftime("%Y%m%d")
# date_string = "20221219"

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

pixel_use = {
    "date": date_string,
    "quantity": input("How many seminars did you do today? :")
}

response = requests.post(url=post_pixel_endpoint, json=pixel_use, headers=headers)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date_string}"

quant = {
    "quantity": "7"
}


delete_pixel = update_pixel_endpoint



print(response.text)
