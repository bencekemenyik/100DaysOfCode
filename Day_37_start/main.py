import requests
from datetime import datetime


PIXELA_ENDPOINT_ACC_CREATE = "https://pixe.la/v1/users"
TOKEN = "your-pixela-token"
USERNAME = "your-pixela-username"

# https://pixe.la/@username

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=PIXELA_ENDPOINT_ACC_CREATE, json=user_params)
# print(response.status_code)
# response.raise_for_status()
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT_ACC_CREATE}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Eating Graph",
    "unit": "calory",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# today = datetime.now()
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many calories did you eat today?"),
}


print(today.strftime("%Y%m%d"))

update_pixel = {
    "quantity": "500"
}

response = requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", json=pixel_config, headers=headers)
print(response.text)

# response = requests.put(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{today.strftime('%Y%m%d')}", headers=headers, json=update_pixel)
# print(response.text)

# response = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{today.strftime('%Y%m%d')}", headers=headers)
# print(response.text)

