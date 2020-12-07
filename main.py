import requests
import os
from twilio.rest import Client

# open weather map api
api_key = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# twilio api
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
account_sid = "AC1940bb58ee26f57f2ed87c48ccf402d6"
from_num = "+15345444344"
to_num = "+15206390031"

# Tucson, AZ
lat = 32.291611
lon = -110.838051

parameters = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "units": "imperial",
    "appid": api_key,
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                     body="It's going to 🌧 today. Bring an ☔.",
                     from_=from_num,
                     to=to_num
                 )
    print(message.status)
