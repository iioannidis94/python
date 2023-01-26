import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "email"
MY_PASS = "pass"
MY_LAT = 38.075974
MY_LNG = 23.745718


def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]

    longitude = float(data["longitude"])
    latitude = float(data["latitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LNG-5 <= longitude <= MY_LNG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0]) + 2
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0]) + 2

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_above() and is_night():

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject:ISS IS ABOVE YOUR HEAD! \n\nLook up ISS is in your sky view!!!!!"
                )

# run the code every 120 seconds
