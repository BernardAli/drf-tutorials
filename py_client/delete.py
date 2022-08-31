import requests

product_id = input("What is the product id you want to delete")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://127.0.0.1:8000/products/{product_id}/delete"

get_response = requests.delete(endpoint) # HTTP Response
print(get_response.json()) # print raw text
print(get_response.status_code) # print status_code