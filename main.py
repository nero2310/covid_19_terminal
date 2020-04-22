import requests

from settings import KEY
url = "https://covid-19-data.p.rapidapi.com/country"
country="Poland"
querystring = {"format":"json","name":country}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key':KEY
    }

response = requests.request("GET", url, headers=headers,params=querystring)

print(response.text)