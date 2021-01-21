import requests
from twilio.rest import Client
#Co ordinates latitude and longitude
LAT = ***************
LONG = ***************
API_KEY = "***************************"#your Api Key Open weather maps api
param = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
will_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=param)
response.raise_for_status()
data = response.json()
next_twelve_hours_climate = data["hourly"][:12]
for hour_data in next_twelve_hours_climate:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    account_sid = "*************************"#twilio sid
    auth_token = "******************"#twilio Token
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's Going to Rain Carry Umbrella ☔",
        from_="**********",#twilio ph no
        to="***********",#your ph/mobile no
    )
    print(message.status)