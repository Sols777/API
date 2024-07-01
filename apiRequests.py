import requests


# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
endpoint = "https://api.sunrise-sunset.org/json"

parameters = {
    'lat' : 41.150130,
    'lng' : -8.653090,
}

response = requests.get(url = endpoint , params = parameters)
data = response.json()

print(data)