import requests
import os
from twilio.rest import Client

account_sid = "your-account-sid"
auth_token = "your-auth-token"




parameters = {
    "lat": 47.1994,
    "lon": 18.1395,
    "appid": "01bc29cfcd2508bd84c02f006ab6d4fd",
    "units": "metric",
    "exclude": "current,minutely,daily,alerts"
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()

data = response.json()

twelve_hour_forecast = data["hourly"][:12]

hourly_temp_list = [hourly_dict["temp"] for hourly_dict in data["hourly"][:24]]
hourly_description_list = [hourly_forecast["weather"][0]["description"] for hourly_forecast in twelve_hour_forecast if hourly_forecast["weather"][0]["id"] < 700]


print(max(hourly_temp_list))
print(hourly_description_list)
if len(hourly_description_list) > 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='your-trial-number',
        to='your-number'
    )
    print(message.status)


