import requests
from twilio.rest import Client

# the parameter name must be equal to the api"s documentation
def api_weather_connection():
    ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
    PARAMS = {
        "lat": 41.385063,
        "lon": 2.173404,
        "appid": "",
        "cnt":4
    }
    api = requests.get(ENDPOINT, params=PARAMS)
    api.raise_for_status()
    return api.json()

def check_rain(connection):
    will_rain = False
    for hour_data in connection["list"]:
        condition = hour_data["weather"][0]["id"]
        if int(condition) < 700:
            will_rain = True
    return will_rain

def send_sms():
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body = "Will be raining in the next 12h, better bring an umbrella if your going out",
    from_="+",
    to="+"
    )

    return message.status

#Creating connection       
if check_rain(api_weather_connection()):
    print(send_sms())
