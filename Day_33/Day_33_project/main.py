import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 41.390205
MY_LONG = 2.154007

SENDER = ""
PASSWORD = "*"
RECEIVER = ""

#understanding if iss is in my location
def is_iss():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response.raise_for_status()) >>>>> will raise the error if != from 200
    data = response_iss.json()  # geting json
    longitude_iss = float(data['iss_position']['longitude'])  # getting only the 'longitude' of the iss
    latitude_iss = float(data['iss_position']['latitude'])
    if (MY_LONG - 5) <= longitude_iss <= (MY_LONG + 5) and (MY_LAT - 5) <= latitude_iss <= (MY_LAT + 5):     
        return True

#understanding if it's night (iss can be only seen by night)
def is_night():
    my_location = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=my_location)
    data_sun = response_sun.json()

    # getting just the hours for sunset and sunrise
    sunrise = int(data_sun['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data_sun['results']['sunset'].split("T")[1].split(":")[0])

    timenow = datetime.now().hour

    if timenow >= sunset or timenow <= sunrise:
        return True


def send_email_now():

    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        #securing the connection (encrypt the message if intercepted)
        connection.starttls()
        #loggin 
        connection.login(user=SENDER, password=PASSWORD)
     
        email_content = f"Subject: ISS in your area!\n\nTime to look up!\nThe iss is passing by you."

        connection.sendmail(from_addr=SENDER, to_addrs=RECEIVER, msg=email_content.encode('utf-8'))


while True:
    time.sleep(60)
    if is_iss() ==True and is_night() ==True:
        send_email_now()

