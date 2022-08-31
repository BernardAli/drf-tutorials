import requests


endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title": "keyboard", "content": "Hello World", "price": 150}) # HTTP Response
print(get_response.json()) # print raw text
print(get_response.status_code) # print status_code