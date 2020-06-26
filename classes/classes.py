import requests
import json

from settings import API_KEY

if __name__ == "__main__":
    print("Don't run this file directly, run main.py instead")


def get_list_of_countries():  # toDo find a way to properly format output text
    url = "https://covid-19-data.p.rapidapi.com/help/countries"
    query = {"format": "json"}
    headers = {
        "x-rapidapi-host": "covid-19-data.p.rapidapi.com",
        "x-rapidapi-key": API_KEY,
    }
    response = requests.request("GET", url, headers=headers, params=query)
    json_response = json.dumps(response.json())
    with (open("../countires.json", "w")) as file:
        for element in json_response:
            file.write(str(element))
    return response.text


