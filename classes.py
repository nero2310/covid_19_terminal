import requests
import json
from datetime import date, timedelta, datetime

from settings import API_KEY


def get_list_of_countries():  # toDo find a way to properly format output text
	url = "https://covid-19-data.p.rapidapi.com/help/countries"
	query = {"format": "json"}
	headers = {
		'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
		'x-rapidapi-key': API_KEY
	}
	response = requests.request("GET", url, headers=headers, params=query)
	json_response = json.dumps(response.json())
	with(open("countires.json", "w")) as file:
		for element in json_response:
			file.write(str(element))
	return response.text


class DateAnalyzer:
	def __init__(self, data):
		self.json_obj = data
		self.cases_dict = self.json_obj[0]

	def print_json(self):
		for key, value in self.cases_dict.items():
			print(key, value)
		return 1

	def cases_validity(self):  # If active/confirmed cases are equal 0 print warning
		if self.cases_dict.get("confirmed", 0) == False | self.cases_dict.get("recovered", 0) == False:
			print("Warning don't have data from this date check another day")
			print("Check day before")
			return False
		else:
			return True


class BaseApiClass:
	def __init__(self):
		print("Init")
		self.date_today = date.today()
		self.yesterday = date.today() - timedelta(days=1)
		self.date_today, self.yesterday = self.date_today.strftime("%Y-%m-%d"), self.yesterday.strftime("%Y-%m-%d")
		self.headers = {
			'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
			'x-rapidapi-key': API_KEY
		}
		self.query = {}
		self.url = ""
		self.date = date.today()

	def make_a_call(self):
		self.response = requests.request("GET", self.url, headers=self.headers, params=self.query)
		json_obj = json.loads(self.response.text)
		data = DateAnalyzer(json_obj)
		if data.cases_validity():
			data.print_json()

	def set_date(self):
		variable = input("Enter date example 2020-5-15 : ") # I know it's ugly way to pass a value but i don't have idea																							# how to pass date
		self.date = datetime.strptime(variable, "%Y-%m-%d").date()


class TotalCases(BaseApiClass, DateAnalyzer):
	def __init__(self):
		super().__init__()
		self.query = {"format": "json"}
		self.url = "https://covid-19-data.p.rapidapi.com/totals"

	def print_headers(self):
		print(self.headers)


class CasesDailyWorld(BaseApiClass, DateAnalyzer):
	def __init__(self):
		super().__init__()
		self.set_date()
		self.query = {"date-format": "YYYY-MM-DD", "format": "json", "date": self.date}
		self.url = "https://covid-19-data.p.rapidapi.com/report/totals"
		print(self.date)
# class
