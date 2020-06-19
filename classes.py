import requests
import json
import pandas as pd
import os.path
import builtins
import pymongo

from datetime import date, timedelta, datetime

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
    with (open("countires.json", "w")) as file:
        for element in json_response:
            file.write(str(element))
    return response.text


class DateAnalyzer:
    def __init__(self, data):
        try:
            self.json_obj = data
            self.cases_dict = self.json_obj[0]
        except KeyError:
            print("Key error")

    def print_json(self):
        try:
            for key, value in self.cases_dict.items():
                print(key, value)
            return 1
        except AttributeError:
            print("No json to print")

    def print_provinces(self):
        for key, value in self.cases_dict.items():
            if key != "provinces":
                print(key, value)
        for element in self.cases_dict["provinces"]:
            if builtins.isinstance(element, dict):
                for key, value in element.items():
                    print(key, value)

    def cases_validity(self):  # If active/confirmed cases are equal 0 print warning
        if (
                self.cases_dict.get("confirmed", 0)
                is False | self.cases_dict.get("recovered", 0)
                is False
        ):
            print("Warning don't have data from this date check another day")
            print("Check day before")
            return False
        else:
            return True


class BaseApiClass:
    """
    Parent class only for inheritance
    This class set default data for attributes like date_today, yesterday , headers , country
    """

    def __init__(self):
        self.date_today = date.today()
        self.yesterday = date.today() - timedelta(days=1)
        self.date_today, self.yesterday = (
            self.date_today.strftime("%Y-%m-%d"),
            self.yesterday.strftime("%Y-%m-%d"),
        )
        self.headers = {
            "x-rapidapi-host": "covid-19-data.p.rapidapi.com",
            "x-rapidapi-key": API_KEY,
        }
        self.query = {}
        self.url = ""
        self.date = date.today()  # Set self.date to today date
        self.country = "Poland"  # It's only default value you should change it by call set_country method

    def make_a_call(self):
        """
        Make a request to api provider
        :return:
        data
        """
        self.response = requests.request(
            "GET", self.url, headers=self.headers, params=self.query
        )
        data = json.loads(self.response.text)
        return data

    def set_date(self, date):
        """
        User set date whose will be used to make a request
        """
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.query["date"] = self.date

    def set_country(self):
        """
        User set country whose will be used to make a request
        """
        country = input("Enter country example Poland : ")
        self.country = country
        self.query = {"format": "json"}
        self.url = "https://covid-19-data.p.rapidapi.com/totals"


class CasesInWorld(BaseApiClass, DateAnalyzer):
    """
    Class whose is used to make a call about daily cases in world
    """

    def __init__(self):
        super().__init__()
        self.url = "https://covid-19-data.p.rapidapi.com/totals"

    def print_headers(self):
        print(self.headers)


class CasesDailyWorld(BaseApiClass, DateAnalyzer):
    """
    Class whose is used to make a call about COVID-19 cases in world, user specify date
    """

    def __init__(self):
        super().__init__()
        self.query = {"date-format": "YYYY-MM-DD", "format": "json", "date": self.date}
        self.url = "https://covid-19-data.p.rapidapi.com/report/totals"


class CasesDailyCountry(
    BaseApiClass, DateAnalyzer
):  # toDo i must overwrite function cases_validity for this class,
    # this class storage date in diffrent way
    """
    Class whose is used to make a call about COVID-19 cases in country, user specify country and date
    """

    def __init__(self):
        super().__init__()
        self.set_country()
        self.query = {
            "date-format": "YYYY-MM-DD",
            "format": "json",
            "date": self.date,
            "name": self.country,
        }
        self.url = "https://covid-19-data.p.rapidapi.com/report/country/name"


class CasesInTimePeriod:  # need to finish this class , maybe make funtion from this class ?
    def __init__(self, start_data: date, end_data: datetime):
        if start_data > end_data:
            print("End date can't be earlier than start date")
            return 1
        else:
            pass


class PandasDataAnalyzer:
    def __init__(self, data):
        index_key = data[0].pop("lastChange")
        self.data_frame = pd.DataFrame(data, index=[index_key])

    def save_to_json(self, file_name="database.json"):
        if not os.path.isfile(file_name):
            try:
                self.data_frame.to_json(path_or_buf=file_name)
            except:
                pass

    def load_from_json(self):
        pass

    def print_data_frame(self):
        print(self.data_frame)


class SaveDataToMongo:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = client["covid_19_db"]
        self.colection = mydb["test"]

    def insert_data(self, data):
        self.colection.insert_one(data)

