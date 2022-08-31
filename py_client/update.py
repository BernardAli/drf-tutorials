import requests


endpoint = "http://127.0.0.1:8000/products/1/update/"

data = {
    "title": "WIFI",
    "price": 99
}

get_response = requests.put(endpoint, json=data) # HTTP Response
print(get_response.json()) # print raw text
print(get_response.status_code) # print status_code