import requests


endpoint = "http://127.0.0.1:8000/products/"

data = {
    "title": "Montior",
    "price": 250
}

get_response = requests.post(endpoint, json=data) # HTTP Response
print(get_response.json()) # print raw text
print(get_response.status_code) # print status_code