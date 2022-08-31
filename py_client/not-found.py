import requests


endpoint = "http://127.0.0.1:8000/products/103"

get_response = requests.get(endpoint) # HTTP Response
print(get_response.json()) # print raw text
print(get_response.status_code) # print status_code