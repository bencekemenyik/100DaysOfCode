import requests
from datetime import datetime
import smtplib

MY_LAT = 47.197659 # Your latitude
MY_LONG = 18.139420 # Your longitude
MY_EMAIL = "your-email"
MY_PASSWORD = "your-password"

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) \
            and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    return False

def is_it_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True
    return False




#If the ISS is close to my current position
if is_iss_overhead() and is_it_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS notify\n\nHey Dummy,\nLook up and you might spot the ISS\nBye")
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



