import requests

API_KEY = "a1a6485a3a223ab7a2cc4eb56e6d3e3f"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
LAT = 32.291611
LONG = -110.838051

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
print(response.status_code)
data = response.json()
print(data)
