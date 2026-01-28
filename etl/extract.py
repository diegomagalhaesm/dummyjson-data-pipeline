import requests

def get_orders():
    url = "https://dummyjson.com/carts"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["carts"]
