import requests

API_KEY = "a1a6485a3a223ab7a2cc4eb56e6d3e3f"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
LAT = 17.45
LONG = 124.7

parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily",
    "units": "imperial",
    "appid": API_KEY,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")


