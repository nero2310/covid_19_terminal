import requests

from settings import KEY
url = "https://covid-19-data.p.rapidapi.com/docs.json"

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key':KEY
    }

response = requests.request("GET", url, headers=headers)

print(response.text)