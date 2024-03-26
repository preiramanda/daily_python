import requests

PARAMETERS = {
"amount": 20,
"type": "boolean",
"category": 12
}
api = requests.get("https://opentdb.com/api.php", params=PARAMETERS)

question_data = api.json()["results"]



